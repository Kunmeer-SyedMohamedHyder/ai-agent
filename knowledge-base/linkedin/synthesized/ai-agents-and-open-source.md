# AI agents & open-source work

Syed's most current and differentiating work is in GenAI and AI agents.

## Open-source: OpenAI Agents SDK
His first open-source contributions to a major AI-agents framework (the OpenAI
Agents SDK, Python):
- **PR #1250** — fixed a bug in `invoke_mcp_tool` where a branch of structured
  content was unreachable.
- **PR #1192** — allowed `trace_include_sensitive_data` to be configured via an
  environment variable.
- Proposed adding the **A2A (Agent-to-Agent) protocol** to the SDK; it wasn't
  merged (it didn't fit the SDK's direction) but the discussion reached the front
  of **Hacker News**.

This gives him hands-on depth with the OpenAI Agents SDK and MCP (Model Context
Protocol) tooling — the same ecosystem modern agentic systems are built on.

## Research: enterprise agent interoperability (SAUL)
He researched how AI agents can be **registered, discovered, and reused** across an
organization instead of staying siloed — a central "smart agent" that either routes
a user to the right agent or delegates between agents using A2A handoff, with an
agent registry exposed over REST and MCP. The vendor-neutral research write-up,
**SAUL (Smart Agent for Unified Liaison)**, was turned into an academic paper
(submitted to an IEEE conference) with a reproducible evaluation showing the
approach scaling from tens to ~90 agents.

## Applied projects
- **Career Bot** — a personal AI agent that answers questions about Syed from his
  own professional data (this project; being upgraded to the OpenAI Agents SDK with
  a wiki-style knowledge base and real tools like meeting scheduling).
- **FlightAI** — a multilingual, voice-enabled flight-booking assistant (Gradio +
  LLM) with side-by-side English/translated chat.

## The through-line
Across all of it, Syed keeps pushing the same idea: **make AI agents reliable and
interoperable in real systems** — orchestration, the MCP/A2A plumbing, and keeping
a human in control — not just demos.
