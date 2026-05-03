# Endpoint Status Cards

Status: `dry_run_endpoint_cards_closed_until_human_yes`

These copy/paste-safe Unicode cards give builders a consistent way to show which Sonic-Forage workflow lane is selected without exposing endpoint URLs or opening a live backend. They are display-only blocks for READMEs, issue comments, terminal demos, and proof decks.

## Global safety contract

- `requires_human_approval: true`
- `starts_gpu: false`
- `starts_paid_api: false`
- `publishes_stream: false`
- `records_audio: false`
- `uploads_private_media: false`
- `downloads_models: false`
- `starts_training: false`
- `mutates_cron: false`
- Endpoint URLs, tokens, private media paths, and credentials stay in local environment variables only.

## ComfyUI visual workflow card

```text
╭─ 🧠 COMFYUI VISUAL LANE ─────────────────────╮
│ status: closed_until_human_yes                │
│ env: COMFYUI_BASE_URL + COMFYUI_ENABLE_PROMPT │
│ proof: docs/integrations/COMFYUI_ENDPOINT_CONTRACT.md │
│ dry-run: parse registry, inspect payload, do not POST /prompt │
│ blocked: GPU start • model download • private upload • generation │
╰───────────────────────────────────────────────╯
```

Human approval question: `Do you approve exactly one ComfyUI generation lane, with the selected workflow ID, prompt text, model/download plan, and output path reviewed first?`

## Synthetic voice/TTS card

```text
╭─ 🔊 SYNTHETIC VOICE LANE ─────────────────────╮
│ status: closed_until_human_yes                │
│ env: VOICE_TTS_BASE_URL + VOICE_TTS_ENABLE_GENERATION │
│ proof: docs/integrations/VOICE_WORKFLOW_CONTRACT.md   │
│ dry-run: validate synthetic descriptor payload only    │
│ blocked: voice clone • named-person imitation • recording/upload │
╰───────────────────────────────────────────────╯
```

Human approval question: `Do you approve one synthetic TTS generation using only synthetic descriptors, no named-person imitation, and no live microphone capture?`

## Realtime command-router card

```text
╭─ 🕹 REALTIME COMMAND ROUTER ──────────────────╮
│ status: closed_until_human_yes                │
│ env: REALTIME_ROUTER_BASE_URL + disabled mic/ws/osc/shell switches │
│ proof: docs/integrations/REALTIME_COMMAND_ROUTER_CONTRACT.md       │
│ dry-run: local JSON fixture -> allowlist decision envelope          │
│ blocked: voice-to-shell • outreach • posting • wallet/keys • cron  │
╰───────────────────────────────────────────────╯
```

Human approval question: `Do you approve one local realtime adapter lane, with microphone, WebSocket, OSC, shell, posting, and cron switches still explicitly reviewed?`

## GitHub builder task card

```text
╭─ 🛠 GITHUB BUILDER TASK ──────────────────────╮
│ status: local_draft_or_public_safe_contribution │
│ repo: https://github.com/Sonic-Forage/rave-culture-field-guide │
│ payload: framework/payloads/github-builder-task.payload.example.json │
│ proof: run scripts/verify.py + scripts/verify_framework.py           │
│ blocked: mass issues • outreach • secret printing • private details │
╰───────────────────────────────────────────────╯
```

Human approval question: `Do you approve this exact GitHub contribution scope and confirm it does not disclose private scene details, credentials, contacts, payment links, or active underground locations?`

## Operator copy rule

When pasting these cards into an issue, README, or launch deck, include the relevant proof path and keep `closed_until_human_yes` visible until an awake human explicitly opens one lane. Do not replace env var names with real endpoints in public docs.
