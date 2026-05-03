#!/usr/bin/env python3
from pathlib import Path
import re, json, sys

ROOT = Path(__file__).resolve().parents[1]
required = [
    'README.md',
    'LICENSE',
    'docs/history/ORIGINS_TO_NOW.md',
    'docs/history/TIMELINE.md',
    'docs/legal-and-safety/RAVE_ACT_AND_POLICY.md',
    'docs/legal-and-safety/HARM_REDUCTION.md',
    'docs/culture/PLUR_AND_COMMUNITY.md',
    'docs/dj/HOW_TO_DJ.md',
    'docs/dj/DJ_TERMINOLOGY.md',
    'docs/sources/SOURCES.md',
    'data/timeline.json',
    'assets/images/rave-culture-timeline-hero.png',
    'CONTRIBUTING.md',
    '.github/ISSUE_TEMPLATE/config.yml',
    '.github/ISSUE_TEMPLATE/city_chapter.yml',
    '.github/ISSUE_TEMPLATE/correction_or_source.yml',
    '.github/ISSUE_TEMPLATE/dj_term_or_guide_improvement.yml',
    'docs/community/CITY_CHAPTER_TEMPLATE.md',
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
errors = []
for rel in required:
    if not (ROOT / rel).exists():
        errors.append(f'missing required file: {rel}')

# Validate JSON
try:
    data = json.loads((ROOT/'data/timeline.json').read_text())
    if not isinstance(data, list) or len(data) < 10:
        errors.append('timeline.json should be a list with at least 10 events')
except Exception as e:
    errors.append(f'timeline.json invalid: {e}')

# Basic markdown link target check for local relative links/images
for md in ROOT.rglob('*.md'):
    text = md.read_text(errors='replace')
    for target in re.findall(r'!\[[^\]]*\]\(([^)]+)\)|\[[^\]]+\]\(([^)]+)\)', text):
        url = target[0] or target[1]
        if url.startswith(('http://','https://','#','mailto:')):
            continue
        clean = url.split('#')[0]
        if clean and not (md.parent / clean).resolve().exists():
            errors.append(f'broken local link in {md.relative_to(ROOT)}: {url}')

# Basic content sanity
readme = (ROOT/'README.md').read_text(errors='replace') if (ROOT/'README.md').exists() else ''
for term in ['RAVE Act', 'PLUR', 'DJ', 'harm-reduction', 'rave culture']:
    if term.lower() not in readme.lower():
        errors.append(f'README missing term: {term}')

if errors:
    print('VERIFY FAILED')
    for e in errors:
        print('-', e)
    sys.exit(1)
print('VERIFY OK')
print(f'root: {ROOT}')
print(f'markdown files: {len(list(ROOT.rglob("*.md")))}')
print(f'timeline events: {len(json.loads((ROOT/"data/timeline.json").read_text()))}')
