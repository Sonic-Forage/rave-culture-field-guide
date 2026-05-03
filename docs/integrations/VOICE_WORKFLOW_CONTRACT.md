# Voice Workflow Contract

Status: synthetic voice draft / operator-armed only.

Voice workflows should be easy to switch between local TTS, OmniVoice, ComfyUI voice nodes, or future endpoints without changing public docs.

## Environment variables only

```bash
VOICE_TTS_BASE_URL=http://127.0.0.1:7860
VOICE_TTS_BACKEND=local_or_omnivoice
VOICE_TTS_ENABLE_GENERATION=false
VOICE_TTS_VOICE=synthetic_host
```

## Rules

- Synthetic voices only by default.
- Do not clone or imitate a real person without explicit rights and approval.
- Do not upload private voice samples while unattended.
- Keep personality in spoken text; keep `voice_instruct` as supported tags.

## Example OmniVoice-style tag set

```text
male, young adult, moderate pitch, american accent
female, elderly, high pitch, british accent, whisper
male, middle-aged, low pitch, australian accent
```

## Closed flags

- uses_real_person_likeness: false
- uploads_private_media: false
- starts_paid_api: false
- records_audio: false
- publishes_stream: false
- requires_human_approval: true
