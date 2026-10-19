"""Run isolated one-turn A/B tasks; source and output roots are explicit arguments."""
from pathlib import Path, PureWindowsPath
from concurrent.futures import ThreadPoolExecutor, as_completed
import argparse
import hashlib
import json
import shutil
import subprocess
import time

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('repo', type=Path)
    parser.add_argument('--workers', type=int, default=3)
    args = parser.parse_args()
    repo = args.repo.resolve()
    suite = repo / 'evals/evals.json'
    skill = repo / 'skills/podium'
    baseline = repo / 'evals/independent-review-iteration-1/evaluation.json'
    cases = json.loads(suite.read_text(encoding='utf-8'))['evals']
    assert len(cases) == 11 and sum(len(c['expectations']) for c in cases) == 55
    assert baseline.is_file()
    out = repo / 'evals/independent-review-iteration-2'
    out.mkdir(exist_ok=True)
    snapshot = out / 'harness/skill-source'
    assert not snapshot.exists(), 'Do not overwrite an existing run.'
    shutil.copytree(skill, snapshot)
    shutil.copy2(Path(__file__), out / 'harness/run_evals.py')
    frozen = {str(p.relative_to(repo)): digest(p) for p in [suite, baseline, *skill.rglob('*')] if p.is_file()}
    (out / 'harness/suite.json').write_bytes(suite.read_bytes())
    disabled = []
    for root in [Path(r'C:\Users\Janiz\.codex\skills'), Path(r'C:\Users\Janiz\.agents\skills')]:
        if root.exists():
            disabled += [str(p).replace('\\', '/') for p in root.rglob('SKILL.md')]
    skills_config = '[' + ','.join('{path=' + json.dumps(p) + ',enabled=false}' for p in disabled) + ']'
    features = ['apps', 'plugins', 'memories', 'skill_search', 'multi_agent', 'browser_use', 'browser_use_external', 'computer_use', 'in_app_browser', 'image_generation', 'recommended_plugins', 'hooks', 'shell_snapshot']
    exe = r'C:\Users\Janiz\AppData\Local\Programs\OpenAI\Codex\bin\codex.exe'
    schema = {'type':'object', 'properties': {'response': {'type':'string'}, 'files': {'type':'array','items':{'type':'object','properties':{'path':{'type':'string'},'content':{'type':'string'}},'required':['path','content'],'additionalProperties':False}}}, 'required':['response','files'], 'additionalProperties':False}
    schema_path = out / 'harness/delivery-schema.json'
    schema_path.write_text(json.dumps(schema,indent=2),encoding='utf-8')
    common = [exe, '-a', 'never', 'exec', '--ignore-user-config', '--ignore-rules', '--ephemeral', '--skip-git-repo-check', '--sandbox', 'read-only', '--json', '--color', 'never', '-m', 'gpt-5.6-sol', '-c', 'model_reasoning_effort="xhigh"', '-c', 'project_doc_max_bytes=0', '-c', 'skills.config=' + skills_config, '--output-schema', str(schema_path)]
    for feature in features:
        common += ['--disable', feature]
    wrapper = ('Work on the following single-turn request. The current date is 2026-10-19, timezone Europe/Kyiv. '
               'File delivery is available through the final response schema: put each deliverable in files as its relative path and complete UTF-8 text content; the host will save those bytes beneath the current directory. '
               'Do not use shell commands or patch tools to write files: this host delivers your files from the schema instead. '
               'Put your final user-facing chat reply in response; the host will save it as response.md. Do not also include response.md in files. '
               'You may read explicitly supplied UTF-8 task input files. Do not inspect the parent repository, other runs, grading files, or unrelated sources. '
               'Use only the request and any explicitly supplied task input below. If you need the user to answer questions, ask them and end this turn; no user answer is supplied.\n\n')
    provenance = {'model': 'gpt-5.6-sol', 'reasoning_effort': 'xhigh', 'cli_version': subprocess.check_output([exe, '--version'], text=True).strip(), 'branch': subprocess.check_output(['git', 'branch', '--show-current'], cwd=repo, text=True).strip(), 'commit': subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=repo, text=True).strip(), 'source_sha256': frozen, 'disabled_skills': disabled, 'disabled_features': features, 'config_docs': 'https://developers.openai.com/codex/config-reference', 'wrapper': wrapper, 'conditions': 'Skill catalogs and repository AGENTS instructions, apps, plugins and configured MCP servers are disabled; shared account-level generic instructions may remain. Only A receives the copied podium skill. No slide-building integration is supplied, including case 5. Agents deliver files as schema text; the host materializes them without editing content. No expectations or expected_output are sent to agents. Preliminary filesystem-tool runs were excluded because the CLI advertised read-only permissions despite the workspace-write flag.', 'runs': []}
    def run(case, variant):
        run_dir = out / f"eval-{case['id']}" / variant
        outputs = run_dir / 'outputs'
        outputs.mkdir(parents=True, exist_ok=False)
        treatment = ('Read and follow the podium skill at ' + str(snapshot / 'SKILL.md') + '. Read its references as needed. These are read-only task inputs.\n\n') if variant == 'A' else ''
        prompt = wrapper + treatment + 'REQUEST:\n' + case['prompt']
        (run_dir / 'input.txt').write_text(prompt, encoding='utf-8')
        reply_path = run_dir / 'reply.json'
        cmd = common + ['-C', str(outputs), '-o', str(reply_path), '-']
        start = time.time()
        with (run_dir / 'events.jsonl').open('w', encoding='utf-8') as stdout, (run_dir / 'stderr.txt').open('w', encoding='utf-8') as stderr:
            process = subprocess.run(cmd, input=prompt, encoding='utf-8', text=True, stdout=stdout, stderr=stderr, timeout=1200)
        payload = json.loads(reply_path.read_text(encoding='utf-8'))
        assert isinstance(payload['response'],str) and isinstance(payload['files'],list)
        destinations=set()
        for item in payload['files']:
            relative=PureWindowsPath(item['path'])
            assert not relative.is_absolute() and not relative.drive and '..' not in relative.parts
            destination=outputs.joinpath(*relative.parts)
            assert destination.resolve().is_relative_to(outputs.resolve()) and destination.name!='response.md'
            assert destination not in destinations
            destinations.add(destination)
            destination.parent.mkdir(parents=True,exist_ok=True)
            destination.write_text(item['content'],encoding='utf-8')
        (outputs/'response.md').write_text(payload['response'],encoding='utf-8')
        result = {'eval': case['id'], 'variant': variant, 'exit_code': process.returncode, 'seconds': round(time.time()-start, 2), 'setup': case.get('setup'), 'response_exists': (outputs/'response.md').is_file(), 'delivered_files':len(payload['files'])}
        (run_dir / 'run.json').write_text(json.dumps(result, indent=2), encoding='utf-8')
        print(json.dumps(result), flush=True)
        return result
    jobs = [(case, v) for case in cases for v in (['A', 'B'] if case['id'] % 2 else ['B', 'A'])]
    errors = []
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(run, case, v): (case['id'], v) for case,v in jobs}
        for future in as_completed(futures):
            try:
                provenance['runs'].append(future.result())
            except Exception as exc:
                errors.append({'run': futures[future], 'error': repr(exc)})
            (out/'harness/provenance.json').write_text(json.dumps(provenance, ensure_ascii=False, indent=2), encoding='utf-8')
    assert all(digest(repo / path) == expected for path,expected in frozen.items()), 'Source changed during execution.'
    assert not errors, errors
    assert len(provenance['runs']) == 22
    assert all(r['exit_code'] == 0 and r['response_exists'] for r in provenance['runs']), 'Some runs did not complete; inspect logs.'

if __name__ == '__main__':
    main()
