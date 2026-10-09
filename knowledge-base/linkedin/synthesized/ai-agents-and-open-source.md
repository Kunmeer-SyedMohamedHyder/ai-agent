# AI agents & open-source work

Syed's most current and differentiating work is in GenAI and AI agents.

His **flagship** here is his own **AI Agent OS** — a personal, production-style
platform of AI agents he built and runs his own work through (this agent runs on
part of it). It's the project he's most proud of; the full story is in
[[building-the-ai-agent-os]].

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

## Open-source: Agent Skills library
He also publishes an open-source **Agent Skills** library — portable, self-contained
`SKILL.md` procedures (document generation, extraction, deck building, and more)
that any capable AI agent can pick up and run. It's his way of packaging hard-won
workflows so other people's agents can reuse them, and it's part of a broader push
toward portable, shareable agent capabilities.

## Current research frontier
Alongside building, Syed runs hands-on research into **making AI agents dependable**
(the kind of work he's preparing to speak about at AI-engineering conferences):
- **Agent reliability / "composure"** — measuring how steady an agent's behaviour is
  from its tool-call trajectory, so you can catch brittle or panicky behaviour
  before it ships.
- **Agent upgrade drift** — detecting when swapping the underlying model quietly
  changes an agent's behaviour, even when the final answer looks the same.
- **A bottom-up agentic enterprise OS** — a real, no-mocks reference build of the
  identity, governance, and shared-memory layers an organisation needs to run many
  agents safely.

## The through-line
Across all of it, Syed keeps pushing the same idea: **make AI agents reliable and
interoperable in real systems** — orchestration, the MCP/A2A plumbing, and keeping
a human in control — not just demos.
