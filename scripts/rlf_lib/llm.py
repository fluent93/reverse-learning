from __future__ import annotations

import os


def call_agent(model_family: str, system: str, user: str) -> str:
    """model_family: 'openai' | 'anthropic'"""
    if model_family == "openai":
        from openai import OpenAI

        client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
        model = os.environ.get("OPENAI_MODEL", "gpt-4o")
        resp = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
            temperature=0.3,
        )
        return resp.choices[0].message.content or ""

    if model_family == "anthropic":
        import anthropic

        client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
        model = os.environ.get("ANTHROPIC_MODEL", "claude-sonnet-4-20250514")
        resp = client.messages.create(
            model=model,
            max_tokens=16000,
            system=system,
            messages=[{"role": "user", "content": user}],
            temperature=0.3,
        )
        parts = [b.text for b in resp.content if hasattr(b, "text")]
        return "\n".join(parts)

    raise ValueError(f"Unknown model_family: {model_family}")


AGENT_MODEL = {
    "drafter": "openai",
    "critic": "anthropic",
    "reviser": "openai",
    "finalist": "anthropic",
    "verifier": "openai",
    "publisher": "anthropic",
}
