# Sonic-Forage Workflow Endpoint Prompt Pack

Status: `workflow_endpoint_prompts_closed_until_human_yes`

Use these prompts when a community builder wants to add or improve an AI workflow lane without exposing real endpoints, starting GPU work, recording audio, uploading private media, or posting publicly. Copy one prompt into a GitHub issue, PR description, local agent task, or command-center card.

## Global safety contract

- Keep endpoint URLs as environment variable names only: `COMFYUI_BASE_URL`, `VOICE_TTS_BASE_URL`, `REALTIME_ROUTER_BASE_URL`, `REALTIME_ROUTER_WS_URL`.
- Use `[REDACTED]` for tokens, private paths, customer data, stream keys, and credentials.
- Default closed switches: `COMFYUI_ENABLE_PROMPT=false`, `VOICE_TTS_ENABLE_GENERATION=false`, `REALTIME_ROUTER_ENABLE_MIC=false`, `REALTIME_ROUTER_ENABLE_SHELL=false`, `PUBLIC_POSTING_APPROVED=false`.
- Do not call `POST /prompt`, start paid/GPU compute, clone a real voice, connect live microphone input, publish a stream, send outreach, create payment links, or mutate cron without an awake human yes.

## Prompt 1 — ComfyUI visual workflow card

```text
Goal: add one forkable ComfyUI visual workflow card for Sonic-Forage.

Create or update a repo-local doc/payload that describes the workflow before any live generation.
Required fields:
- workflow_id:
- output_type: image | video | poster_asset | ui_card
- env var names only: COMFYUI_BASE_URL, COMFYUI_ENABLE_PROMPT, COMFYUI_WORKFLOW_REGISTRY
- read-only proof commands: curl /system_stats, curl /object_info, curl /queue
- normalized dry-run input and output examples
- blocked_without_approval: POST /prompt, model downloads, private reference uploads, remote GPU starts
- closed flags: starts_gpu=false, starts_paid_api=false, publishes_stream=false, records_audio=false, uploads_private_media=false, downloads_models=false, starts_training=false, mutates_cron=false, requires_human_approval=true

Acceptance: link the doc/payload from framework/workflows/workflow-registry.json and run python3 scripts/verify_framework.py.
```

## Prompt 2 — Synthetic voice / TTS lane

```text
Goal: add one synthetic-only voice/TTS workflow lane for Sonic-Forage.

Keep voice identity synthetic and descriptor-based. Do not imitate named people or clone real voices.
Required fields:
- voice_lane_id:
- voice_instruct or descriptor allowlist:
- env var names only: VOICE_TTS_BASE_URL, VOICE_TTS_BACKEND, VOICE_TTS_ENABLE_GENERATION, VOICE_TTS_VOICE
- dry-run spoken text sample suitable for a public-safe demo
- normalized dry-run output with files=[] and prompt_id=null
- blocked_without_approval: voice cloning, named-person imitation, live microphone recording, public audio upload/posting
- closed flags: starts_gpu=false, starts_paid_api=false, publishes_stream=false, records_audio=false, uploads_private_media=false, downloads_models=false, starts_training=false, mutates_cron=false, requires_human_approval=true

Acceptance: update the workflow registry and verify that no real endpoint URL or token appears in git.
```

## Prompt 3 — Realtime voice / OSC / WebSocket command route

```text
Goal: add one low-risk realtime command route to the local fixture router contract.

Define the route before connecting microphone, WebSocket, OSC hardware, shell, or external providers.
Required fields:
- intent:
- required_args:
- risk_level: low | medium | blocked
- requires_confirmation:
- target_route: dashboard.status | drop.preview | agent.pause_requested | reject_unknown_intent
- sample utterances:
- redaction rules for token/key/path-looking args
- blocked_without_approval: shell execution, secret printing, public posting, outreach, live microphone recording, cron mutation
- closed flags: starts_gpu=false, starts_paid_api=false, publishes_stream=false, records_audio=false, uploads_private_media=false, starts_training=false, mutates_cron=false, requires_human_approval=true

Acceptance: add an offline JSON fixture first; unknown or risky commands must reject by default.
```

## Prompt 4 — GitHub builder payload polish

```text
Goal: improve one public-safe builder payload, tag dictionary, Unicode UI block, or workflow contract.

Constraints:
- one small contribution only
- cite repo-local proof paths
- keep all external action lanes closed_until_human_yes
- do not create outreach, payment, public posting, video upload, model download, training, GPU, or private media actions
- include verifier command(s) and expected success highlights

Acceptance: changed files are discoverable from README.md or docs/framework/OPEN_SOURCE_BUILDER_FRAMEWORK.md, JSON parses, scripts/verify_framework.py passes, and git diff --check passes.
```

## Operator review checklist

- [ ] Artifact is forkable and public-safe.
- [ ] Endpoint fields are env-var names or `[REDACTED]` placeholders only.
- [ ] Risky flags are false and `requires_human_approval: true`.
- [ ] The payload references existing proof paths.
- [ ] Verification commands are included.
- [ ] No private scene details, secrets, raw private media, or live endpoint URLs are committed.
