# Realtime Command Router Contract

Status: `dry-run / local fixture only / closed_until_human_yes`

This contract lets Sonic-Forage builders design a realtime-feeling voice, OSC, WebSocket, or dashboard command lane without connecting speech recognition directly to shell execution or any live external provider.

## Closed flags

```yaml
requires_human_approval: true
starts_gpu: false
starts_paid_api: false
publishes_stream: false
records_audio: false
uploads_private_media: false
downloads_models: false
starts_training: false
voice_to_shell: false
mutates_cron: false
```

## Environment variable names only

Copy these into a local `.env` if an awake operator approves a prototype. Do not commit real endpoints, tokens, room IDs, private media paths, or provider credentials.

```bash
REALTIME_ROUTER_ENABLE_MIC=false
REALTIME_ROUTER_ENABLE_WEBSOCKET=false
REALTIME_ROUTER_ENABLE_OSC=false
REALTIME_ROUTER_ENABLE_SHELL=false
REALTIME_ROUTER_BASE_URL=http://127.0.0.1:8787
REALTIME_ROUTER_WS_URL=ws://127.0.0.1:8787/ws/audio
REALTIME_ROUTER_OSC_TARGET=127.0.0.1:9000
REALTIME_ROUTER_API_TOKEN=[REDACTED]
REALTIME_ROUTER_LEDGER_PATH=logs/realtime-command-router-ledger.jsonl
```

## Human approval question

> Do you approve enabling exactly one realtime input lane for a bounded local demo, with shell execution disabled, public posting disabled, live recording disabled, and all events written to a local redacted ledger?

If the answer is missing, ambiguous, or only implied by enthusiasm, the lane remains closed.

## Allowed dry-run intents

| Intent | Risk | Route | Notes |
| --- | --- | --- | --- |
| `dashboard.status` | low | local dashboard event | Show verification/proof status only. |
| `drop.preview` | low | local preview card | Open or render a draft artifact path already in git. |
| `agent.pause_requested` | medium | local queue note | Request pause; do not kill processes or mutate cron. |
| `reject_unknown_intent` | safe default | no-op | Unknown commands are rejected by default. |

## Blocked without approval

- Shell execution, terminal command construction, or voice-to-shell bridges.
- Public posting, social updates, email/DM outreach, issue spam, or payment links.
- GPU starts, model downloads, training jobs, video/Matrix generation, or private media uploads.
- Live microphone recording, voice cloning, named-person imitation, or storage of raw private audio.
- Printing secrets, tokens, private endpoints, wallet keys, or `.env` contents.
- Cron creation, cron mutation, recurring background jobs, or unattended provider connects.

## Normalized dry-run input

See `framework/payloads/realtime-command-router.payload.example.json`.

```json
{
  "source": "local_fixture_or_dashboard_button",
  "utterance": "show the verified launch proof card",
  "parsed_intent": "dashboard.status",
  "confidence": 0.82,
  "args": {"target_panel": "launch-proof-card"}
}
```

## Normalized dry-run output

```json
{
  "ok": true,
  "event_type": "dashboard.status",
  "transport": "local_json_fixture",
  "warnings": ["Dry-run example only; no microphone, OSC hardware, WebSocket provider, or shell bridge is started."]
}
```

## Operator preflight commands

These commands are local/read-only checks for a future scaffold. They are examples, not proof that a live provider is approved.

```bash
PYTHONDONTWRITEBYTECODE=1 python3 scripts/verify.py
PYTHONDONTWRITEBYTECODE=1 python3 scripts/verify_framework.py
python3 -m json.tool framework/payloads/realtime-command-router.payload.example.json >/tmp/sonic_forage_realtime_payload.json
```

If a future server is added, keep `/health` fail-closed and require it to return `starts_gpu: false`, `starts_paid_api: false`, and `voice_to_shell: false` before any `/api/voice/decide` or `/ws/audio` testing.

## Failure handling

- Unknown intent: return `reject_unknown_intent` and log a redacted no-op entry.
- Secret-looking args: redact keys/values containing `token`, `secret`, `password`, `key`, or endpoint credentials.
- Missing approval: keep `requires_human_approval: true` and do not open microphone/WebSocket/OSC lanes.
- Provider unavailable: degrade to local JSON fixtures and static dashboard cards.
