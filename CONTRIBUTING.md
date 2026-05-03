# Contributing to the Rave Culture Field Guide

Welcome to the community starter kit for the **Sonic-Forage/rave-culture-field-guide** project.

This guide is a living educational resource about rave culture, DJ practice, policy history, harm reduction, and local scene memory. Contributions should help people understand the culture with respect, context, and care.

## Default project home

- GitHub organization: `Sonic-Forage`
- Repository: `Sonic-Forage/rave-culture-field-guide`
- Public URL: https://github.com/Sonic-Forage/rave-culture-field-guide

If you fork, mirror, or reference this project, keep Sonic-Forage as the canonical upstream unless the maintainers say otherwise.

## Good first contributions

- Add a source-backed correction to a date, law, venue, scene, genre, or term.
- Improve the DJ glossary with clear beginner-friendly language.
- Add a city chapter using `docs/community/CITY_CHAPTER_TEMPLATE.md`.
- Add safer-event or accessibility notes backed by credible public resources.
- Improve broken links, typo fixes, or reading-path clarity.

## Cultural contribution standards

Rave history is not one single story. Please write with humility and attribution.

Contributions should:

- Credit Black, Latino, queer, immigrant, working-class, DIY, and local community roots where relevant.
- Avoid flattening underground scenes into commercial festival history only.
- Treat harm reduction as public-health education, not as encouragement of illegal activity.
- Avoid doxxing, private party locations, private crew drama, or unverified allegations.
- Distinguish first-hand memories from source-verified historical claims.
- Use respectful language for people, scenes, genres, and regions.

## Source standards

For factual claims, include at least one public source when possible:

- Books, documentaries, interviews, archives, public museum/library materials.
- Official law/policy pages for legal claims.
- Harm-reduction organizations or public-health resources for safety claims.
- Local flyers/zines/articles only when they are safe and public to share.

If something is oral history or lived memory, label it clearly:

> Local memory / needs source: ...

## How to submit a change

1. Fork the repo.
2. Create a branch with a clear name:
   - `docs/city-detroit-chapter`
   - `fix/rave-act-date-source`
   - `docs/dj-glossary-phrasing`
3. Make your edits.
4. Run the verifier:

   ```bash
   python3 scripts/verify.py
   ```

5. Open a pull request and explain:
   - What changed.
   - Why it improves the guide.
   - Which sources support it.
   - Any safety/cultural context reviewers should know.

## City chapter checklist

Use `docs/community/CITY_CHAPTER_TEMPLATE.md` and include:

- City / region name.
- Short scene overview.
- Key sounds and influences.
- Community values and safer-space notes.
- Public-safe landmarks, archives, or venues.
- Local DJ/producer/radio/zine/flyer context when safe to name.
- Sources and open questions.

Do **not** include private addresses, active underground party locations, personal phone numbers, or anything that could put crews/attendees at risk.

## Maintainer review checklist

Before merging, reviewers should confirm:

- The contribution is public-safe.
- Factual claims are sourced or clearly labeled as memory/open question.
- No credentials, private contact info, private venue locations, or doxxing appear.
- Local links and JSON still pass `python3 scripts/verify.py`.
- Tone matches the field-guide purpose: educational, respectful, useful, and fun.
