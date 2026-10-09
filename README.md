---
title: Ask Syed's AI
emoji: 🤖
colorFrom: blue
colorTo: purple
sdk: gradio
sdk_version: 5.0.1
app_file: app.py
pinned: false
---

# Ask Syed's AI

Syed's personal AI agent. Ask about his experience, projects, AI-agent and
open-source work, how he thinks, and what he's open to — or leave your details and
it will pass them on.

## How it works

- **OpenAI Agents SDK** (no LangChain).
- **Wiki-style knowledge base** (no vector RAG): the agent reads a small set of
  curated, public-safe markdown pages under `knowledge-base/` directly in its
  instructions, so it can only answer from that content.

## Run locally

```bash
pip install -r requirements.txt
export OPENAI_API_KEY=sk-...        # required
python app.py
```

On Hugging Face Spaces, set `OPENAI_API_KEY` as a Space **secret**.

## Knowledge base

Only **public, professional** content lives in `knowledge-base/` (profile,
experience, education, skills, certifications, projects, publications, and
synthesized summaries). Private data (messages, connections, phone/email, etc.) is
intentionally excluded.