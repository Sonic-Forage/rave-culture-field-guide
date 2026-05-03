#!/usr/bin/env python3
from pathlib import Path
import json, sys, re
ROOT = Path(__file__).resolve().parents[1]
required = [
 'docs/framework/OPEN_SOURCE_BUILDER_FRAMEWORK.md',
 'framework/ui/UNICODE_RAVE_UI_KIT.md',
 'framework/ui/ENDPOINT_STATUS_CARDS.md',
 'framework/tags/sonic-forage-tags.json',
 'framework/prompts/github-community-prompts.md',
 'framework/prompts/ai-media-prompts.md',
 'framework/prompts/workflow-endpoint-prompts.md',
 'framework/prompts/voice-persona-prompt-pack.md',
 'framework/payloads/city-chapter.payload.example.json',
 'framework/payloads/workflow-endpoint-task.payload.example.json',
 'framework/payloads/sonic-voice-persona.payload.example.json',
 'framework/payloads/comfyui-dry-run.payload.example.json',
 'framework/payloads/voice-workflow.payload.example.json',
 'framework/payloads/realtime-command-router.payload.example.json',
 'framework/payloads/github-builder-task.payload.example.json',
 'framework/payloads/endpoint-status-card.payload.example.json',
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
workflow_task=json.loads((ROOT/'framework/payloads/workflow-endpoint-task.payload.example.json').read_text())
if workflow_task.get('requires_human_approval') is not True:
    errors.append('workflow endpoint task payload requires_human_approval must be true')
for flag, value in workflow_task.get('flags', {}).items():
    if value is not False:
        errors.append(f'workflow endpoint task risky flag must be false: {flag}')
for proof in workflow_task.get('task_template', {}).get('proof_paths', []):
    if not (ROOT/proof).exists(): errors.append(f'workflow endpoint task proof path missing: {proof}')
for needle in ['COMFYUI_BASE_URL','VOICE_TTS_BASE_URL','REALTIME_ROUTER_BASE_URL','closed_until_human_yes','[REDACTED]']:
    if needle not in json.dumps(workflow_task): errors.append(f'workflow endpoint task missing {needle}')
workflow_prompts=(ROOT/'framework/prompts/workflow-endpoint-prompts.md').read_text(errors='replace')
for needle in ['workflow_endpoint_prompts_closed_until_human_yes','COMFYUI_ENABLE_PROMPT=false','VOICE_TTS_ENABLE_GENERATION=false','REALTIME_ROUTER_ENABLE_SHELL=false','requires_human_approval=true']:
    if needle not in workflow_prompts: errors.append(f'workflow endpoint prompt pack missing {needle}')
voice_persona_prompt=(ROOT/'framework/prompts/voice-persona-prompt-pack.md').read_text(errors='replace')
for needle in ['voice_persona_prompt_pack_closed_until_human_yes','VOICE_TTS_ENABLE_GENERATION=false','VOICE_TTS_BASE_URL=[REDACTED]','requires_human_approval=true','Do not imitate named artists']:
    if needle not in voice_persona_prompt: errors.append(f'voice persona prompt pack missing {needle}')
voice_persona=json.loads((ROOT/'framework/payloads/sonic-voice-persona.payload.example.json').read_text())
if voice_persona.get('requires_human_approval') is not True:
    errors.append('voice persona payload requires_human_approval must be true')
for flag, value in voice_persona.get('flags', {}).items():
    if value is not False:
        errors.append(f'voice persona risky flag must be false: {flag}')
if len(voice_persona.get('personas', [])) < 3:
    errors.append('voice persona payload needs at least 3 personas')
for persona in voice_persona.get('personas', []):
    if not persona.get('voice_instruct') or any(name in persona.get('voice_instruct','').lower() for name in ['artist', 'dj ', 'celebrity', 'clone']):
        errors.append(f"voice persona has unsafe voice_instruct: {persona.get('id')}")
    if len(persona.get('blocked_without_approval', [])) < 4:
        errors.append(f"voice persona blocked list too short: {persona.get('id')}")
for proof in voice_persona.get('proof_paths', []):
    if not (ROOT/proof).exists(): errors.append(f'voice persona proof path missing: {proof}')
for needle in ['VOICE_TTS_BASE_URL','VOICE_TTS_API_TOKEN','[REDACTED]','VOICE_TTS_ENABLE_GENERATION']:
    if needle not in json.dumps(voice_persona): errors.append(f'voice persona payload missing {needle}')
status_cards=json.loads((ROOT/'framework/payloads/endpoint-status-card.payload.example.json').read_text())
if status_cards.get('requires_human_approval') is not True:
    errors.append('endpoint status-card payload requires_human_approval must be true')
for flag, value in status_cards.get('flags', {}).items():
    if value is not False:
        errors.append(f'endpoint status-card risky flag must be false: {flag}')
if len(status_cards.get('cards', [])) < 4:
    errors.append('endpoint status-card payload needs at least 4 cards')
for card in status_cards.get('cards', []):
    if 'closed_until_human_yes' not in card.get('status', '') and 'review' not in card.get('status', ''):
        errors.append(f"endpoint status-card unsafe status: {card.get('id')}")
    if not card.get('env_var_names'):
        errors.append(f"endpoint status-card missing env vars: {card.get('id')}")
    if not card.get('human_approval_question'):
        errors.append(f"endpoint status-card missing approval question: {card.get('id')}")
    if len(card.get('blocked_without_approval', [])) < 3:
        errors.append(f"endpoint status-card blocked list too short: {card.get('id')}")
    for proof in card.get('proof_paths', []):
        if not (ROOT/proof).exists(): errors.append(f"endpoint status-card proof path missing: {proof}")
ui_cards=(ROOT/'framework/ui/ENDPOINT_STATUS_CARDS.md').read_text(errors='replace')
for needle in ['dry_run_endpoint_cards_closed_until_human_yes','COMFYUI_BASE_URL','VOICE_TTS_BASE_URL','REALTIME_ROUTER_BASE_URL','requires_human_approval: true']:
    if needle not in ui_cards: errors.append(f'endpoint status-card UI missing {needle}')
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
