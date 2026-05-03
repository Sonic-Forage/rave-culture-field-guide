#!/usr/bin/env python3
from pathlib import Path
import json, sys, re
ROOT = Path(__file__).resolve().parents[1]
required = [
 'docs/framework/OPEN_SOURCE_BUILDER_FRAMEWORK.md',
 'framework/ui/UNICODE_RAVE_UI_KIT.md',
 'framework/tags/sonic-forage-tags.json',
 'framework/prompts/github-community-prompts.md',
 'framework/prompts/ai-media-prompts.md',
 'framework/payloads/city-chapter.payload.example.json',
 'framework/payloads/comfyui-dry-run.payload.example.json',
 'framework/payloads/voice-workflow.payload.example.json',
 'framework/payloads/realtime-command-router.payload.example.json',
 'framework/workflows/workflow-registry.json',
 'framework/workflows/endpoint-switchboard.example.json',
 'docs/integrations/COMFYUI_ENDPOINT_CONTRACT.md',
 'docs/integrations/VOICE_WORKFLOW_CONTRACT.md',
 'docs/integrations/REALTIME_COMMAND_ROUTER_CONTRACT.md',
 '.env.example',
]
errors=[]
for rel in required:
    if not (ROOT/rel).exists(): errors.append(f'missing framework file: {rel}')
for rel in [p for p in required if p.endswith('.json')]:
    try: json.loads((ROOT/rel).read_text())
    except Exception as e: errors.append(f'invalid json {rel}: {e}')
registry=json.loads((ROOT/'framework/workflows/workflow-registry.json').read_text())
if len(registry.get('workflows', [])) < 3: errors.append('workflow registry needs at least 3 workflows')
for wf in registry.get('workflows', []):
    if not (ROOT/wf.get('payload','')).exists(): errors.append(f"workflow payload missing: {wf.get('id')}")
switchboard=json.loads((ROOT/'framework/workflows/endpoint-switchboard.example.json').read_text())
flags=switchboard.get('global_flags', {})
for flag in ['requires_human_approval','starts_gpu','starts_paid_api','publishes_stream','records_audio','uploads_private_media','downloads_models','starts_training','mutates_cron']:
    if flag not in flags: errors.append(f'endpoint switchboard missing global flag: {flag}')
for flag, value in flags.items():
    if flag == 'requires_human_approval':
        if value is not True: errors.append('endpoint switchboard requires_human_approval must be true')
    elif value is not False:
        errors.append(f'endpoint switchboard risky flag must be false: {flag}')
lanes=switchboard.get('lanes', [])
if len(lanes) < 3: errors.append('endpoint switchboard needs at least 3 lanes')
for lane in lanes:
    if lane.get('status') not in ['closed_until_human_yes','open_for_public_safe_contribution']:
        errors.append(f"endpoint switchboard lane has unsafe status: {lane.get('id')}")
    env_vars=lane.get('env_vars', {})
    if not env_vars: errors.append(f"endpoint switchboard lane missing env vars: {lane.get('id')}")
    for proof in lane.get('proof_paths', []):
        if not (ROOT/proof).exists(): errors.append(f"endpoint switchboard proof path missing: {proof}")
for rel in ['docs/integrations/COMFYUI_ENDPOINT_CONTRACT.md','docs/integrations/VOICE_WORKFLOW_CONTRACT.md','docs/integrations/REALTIME_COMMAND_ROUTER_CONTRACT.md']:
    text=(ROOT/rel).read_text(errors='replace').lower()
    for needle in ['requires_human_approval', 'false', 'closed']:
        if needle not in text: errors.append(f'{rel} missing {needle}')
env=(ROOT/'.env.example').read_text(errors='replace')
for marker in ['COMFYUI_ENABLE_PROMPT=false','VOICE_TTS_ENABLE_GENERATION=false','REALTIME_ROUTER_ENABLE_SHELL=false','PUBLIC_POSTING_APPROVED=false']:
    if marker not in env: errors.append(f'.env.example missing {marker}')
all_text='\n'.join((ROOT/rel).read_text(errors='replace') for rel in required if not rel.endswith('.json'))
if re.search(r'(ghp_|github_pat_|sk-[A-Za-z0-9]|hf_[A-Za-z0-9]|BEGIN [A-Z ]*PRIVATE KEY)', all_text):
    errors.append('secret-looking marker found in framework docs')
if errors:
    print('FRAMEWORK VERIFY FAILED')
    for e in errors: print('-', e)
    sys.exit(1)
print('FRAMEWORK VERIFY OK')
print(f'framework files: {len(required)}')
print(f'workflows: {len(registry.get("workflows", []))}')
