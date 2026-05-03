# Sonic-Forage Voice Persona Prompt Pack

Status: `voice_persona_prompt_pack_closed_until_human_yes`

Use this pack when a builder wants synthetic host/interlude voice copy, voice-design descriptors, or UI-readout scripts for Sonic-Forage without cloning real people, recording private media, or calling a live TTS endpoint by default.

## Safety contract

- `requires_human_approval=true`
- `VOICE_TTS_ENABLE_GENERATION=false`
- `VOICE_TTS_BASE_URL=[REDACTED]`
- `VOICE_TTS_API_TOKEN=[REDACTED]`
- Do not imitate named artists, DJs, public figures, crew members, or private attendees.
- Do not upload private voice samples, field recordings, private party audio, or crowd audio.
- Do not publish generated audio, post clips, or start paid endpoints until an awake human approves exactly one lane.

## Copy/paste prompt: synthetic host voice

```text
You are drafting a synthetic-only Sonic-Forage host voice for a public-safe open-source framework.

Goal:
Create a short spoken intro that welcomes community builders to a rave-culture field guide and explains one safe builder task.

Voice design descriptors only:
Use generic tags such as "male", "female", "young adult", "middle-aged", "low pitch", "moderate pitch", "american accent", "british accent", or "whisper". Do not reference or imitate a real person.

Spoken text constraints:
- 30 seconds or less.
- Mention Sonic-Forage once.
- Say the work is source-backed, public-safe, and closed-by-default.
- No private event locations, no drug-use encouragement, no medical/legal promises, no outreach/payment/public-posting claims.

Output:
Return JSON with voice_instruct, spoken_text, safety_notes, and blocked_without_approval.
```

## Copy/paste prompt: rave UI readout voice

```text
Draft a 10-second synthetic voice readout for a local dashboard card.

Context:
The card summarizes one dry-run workflow endpoint lane: ComfyUI, synthetic voice/TTS, realtime router, GitHub builder task, or endpoint status card.

Required phrases:
- "closed until human yes"
- "env vars only"
- "no paid compute started"

Constraints:
No live endpoint URLs, no tokens, no private media, no voice cloning, no public posting, no payment or outreach call to action.
```

## Copy/paste prompt: persona set builder

```text
Create three synthetic-only Sonic-Forage persona drafts for open-source docs and local demo narration.

Each persona must include:
- id
- display_name
- voice_instruct using generic descriptors only
- allowed_use
- sample_line under 20 words
- blocked_without_approval list
- risky_flags with every risky flag false

Hard blocks:
No real-person likeness, no artist imitation, no voice cloning, no private-media upload, no recording, no live TTS generation, no public posting, no paid API start.
```

## Example descriptor palette

- `female, young adult, moderate pitch, american accent`
- `male, middle-aged, low pitch, british accent`
- `female, elderly, high pitch, whisper`
- `male, young adult, moderate pitch, australian accent`

Keep lore, humor, and Sonic-Forage mythology in `spoken_text`; keep `voice_instruct` limited to generic descriptor tags.
