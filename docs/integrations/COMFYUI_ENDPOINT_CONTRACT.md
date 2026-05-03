# ComfyUI Endpoint Contract

Status: dry-run / operator-armed only.

This repo documents ComfyUI workflow payloads, but it does not call `/prompt` by default.

## Environment variables only

```bash
COMFYUI_BASE_URL=http://127.0.0.1:8188
COMFYUI_ENABLE_PROMPT=false
COMFYUI_WORKFLOW_REGISTRY=framework/workflows/workflow-registry.json
```

Do not commit real remote endpoint URLs, tokens, private media paths, or `.env` files.

## Read-only preflight

```bash
curl -fsS "$COMFYUI_BASE_URL/system_stats"
curl -fsS "$COMFYUI_BASE_URL/object_info" >/tmp/comfy_object_info.json
curl -fsS "$COMFYUI_BASE_URL/queue"
curl -fsS "$COMFYUI_BASE_URL/prompt"
```

## Closed flags

- starts_gpu: false
- starts_paid_api: false
- publishes_stream: false
- records_audio: false
- uploads_private_media: false
- requires_human_approval: true

## Human approval question

"Do you approve calling this exact ComfyUI endpoint with this exact workflow payload, budget/time cap, and output destination?"

## Normalized dry-run output

```json
{
  "ok": true,
  "dry_run": true,
  "prompt_id": null,
  "files": [],
  "warnings": ["/prompt is disabled until COMFYUI_ENABLE_PROMPT=true and human approval is recorded"]
}
```
