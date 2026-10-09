#!/usr/bin/env python3
"""Syed's personal AI agent.

A conversational agent that answers questions about Syed on his behalf, for people
who scan his business card / visit his profile. Built on the OpenAI Agents SDK.

Design: no vector RAG. The knowledge base is a small set of wiki-style markdown
pages that are read from disk and placed directly in the agent's instructions
("wiki-style" grounding). This keeps it simple, cheap, and fully controllable —
the agent can only answer from the curated public pages in ``knowledge-base/``.
"""

from __future__ import annotations

import glob
import os

import gradio as gr
from dotenv import load_dotenv

from agents import Agent, Runner

load_dotenv()

MODEL = os.getenv("AGENT_MODEL", "gpt-4o-mini")
NAME = "K Syed Mohamed Hyder"
KB_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "knowledge-base")


def load_knowledge() -> str:
    """Concatenate every markdown page under knowledge-base/ into one document."""
    parts: list[str] = []
    for path in sorted(glob.glob(os.path.join(KB_DIR, "**", "*.md"), recursive=True)):
        rel = os.path.relpath(path, KB_DIR)
        with open(path, encoding="utf-8") as handle:
            body = handle.read().strip()
        if body:
            parts.append(f"## SOURCE: {rel}\n\n{body}")
    return "\n\n---\n\n".join(parts)


KNOWLEDGE = load_knowledge()

INSTRUCTIONS = f"""You are the personal AI agent for {NAME} — known as Syed. You \
speak on his behalf to people who find his profile or scan his card: recruiters, \
engineers, founders, and potential collaborators.

Your job: answer questions about Syed — his experience, skills, projects, his \
AI-agent and open-source work, how he thinks, and what he is open to — warmly, \
concisely, and honestly, using ONLY the knowledge below. Refer to him as "Syed" \
or "he".

Rules:
- Use ONLY the knowledge provided below. If something is not covered, say you do \
  not have that detail and offer to pass the question on to Syed or point them to \
  his LinkedIn. Never invent facts, employers, dates, numbers, or opinions.
- Never share private or sensitive information (personal phone numbers, home \
  address, finances, or anything not in the knowledge). If asked, politely decline \
  and offer his LinkedIn or to take a message.
- Keep answers short, specific, and friendly. End with a helpful next step where \
  it fits: connect on LinkedIn, or leave their name and what they would like, so \
  Syed can follow up.
- If someone wants to hire or collaborate, be encouraging and point them to the \
  best way to reach him.

=== KNOWLEDGE ABOUT SYED ===
{KNOWLEDGE}
=== END KNOWLEDGE ==="""

agent = Agent(name="Syed's Agent", instructions=INSTRUCTIONS, model=MODEL)


def respond(message: str, history: list[dict]) -> str:
    """Gradio chat handler. ``history`` is a list of {role, content} messages."""
    conversation = [{"role": m["role"], "content": m["content"]} for m in history]
    conversation.append({"role": "user", "content": message})
    result = Runner.run_sync(agent, conversation)
    return result.final_output


demo = gr.ChatInterface(
    fn=respond,
    type="messages",
    title="Ask Syed's AI 🤖",
    description=(
        "Hi! I'm Syed's personal AI agent. Ask me about his experience, projects, "
        "AI-agent and open-source work, or what he's open to — or leave your details "
        "and I'll pass them on."
    ),
    examples=[
        "What does Syed do?",
        "Tell me about his AI-agent and open-source work.",
        "What is he looking for / open to?",
        "What are his strongest skills?",
    ],
)

if __name__ == "__main__":
    demo.launch()
