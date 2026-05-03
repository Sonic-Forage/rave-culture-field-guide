# Sonic-Forage Open Source Builder Framework

Status: public framework starter, community-buildable, closed-gate for live endpoints.

This project is not only a rave-culture guide. It is also an open-source framework for community members to build useful, respectful, public-safe culture tools on top of the guide.

## What builders can extend

- **Prompts** — reusable GitHub issue/PR/research/media prompts.
- **Payloads** — structured JSON payloads for agents, UI cards, ComfyUI dry-runs, voice personas, and city chapters.
- **Tags** — consistent labels for genres, city chapters, safety gates, DJ terms, workflow lanes, and review status.
- **Unicode UI kit** — badass terminal/readme/dashboard blocks that feel rave-native but still copy/paste cleanly.
- **Workflow contracts** — easy-switch endpoint templates for ComfyUI, voice/TTS, and future AI media backends.

## Design principles

1. **Open source first** — make reusable templates that other crews can fork.
2. **Community safety first** — never expose private scene locations, private contacts, credentials, or unapproved media.
3. **Swappable backends** — describe env vars and payloads before hard-coding any endpoint.
4. **Human-gated launch** — public posting, GPU/video generation, payments, outreach, and uploads stay closed until a human says yes.
5. **Proof over hype** — every launch claim should map to a file, URL, command, or verifier output.

## Recommended repo lanes

```text
framework/
  prompts/       # copy/paste prompt packs
  payloads/      # JSON examples and schemas
  tags/          # tag dictionaries and labels
  workflows/     # dry-run endpoint contracts
  ui/            # Unicode UI blocks and readme/dashboard sections
```

## Builder quick start

1. Copy a prompt from `framework/prompts/`.
2. Pick tags from `framework/tags/sonic-forage-tags.json`.
3. Use a payload from `framework/payloads/`.
4. Choose an endpoint lane from `framework/workflows/endpoint-switchboard.example.json` and keep endpoint URLs in environment variables, not git.
5. Leave all switches such as `COMFYUI_ENABLE_PROMPT=false`, `VOICE_TTS_ENABLE_GENERATION=false`, and posting/upload/payment gates closed until an awake operator says yes.
6. Run:

```bash
python3 scripts/verify.py
python3 scripts/verify_framework.py
```

## Closed gates

The framework contains placeholders for AI endpoints and voice workflows, but it does not call live ComfyUI, TTS, GPU, upload, or social APIs by default.
