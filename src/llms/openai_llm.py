# src/llms/openai_llm.py

import os
import openai
from typing import Protocol


class IconLLM(Protocol):
    def generate_icon_svg(self, prompt: str) -> str:
        ...


class OpenAILLM:
    def __init__(self, model="gpt-4", api_key=None):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            # No API key found, mark as unavailable
            self.available = False
        else:
            openai.api_key = self.api_key
            self.available = True

    def generate_icon_svg(self, prompt: str) -> str:
        if not self.available:
            return "<svg><text x='10' y='20' fill='red'>OpenAI API key missing</text></svg>"
        # Your existing OpenAI call here...
        system_prompt = (
            "You are an expert icon designer. "
            "Given a short description of a concept, return only a minimal and clean SVG string "
            "representing a flat icon of it. Only return SVG code. No explanations, no formatting."
        )

        user_prompt = f"Design an SVG icon for: {prompt}"

        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.7,
            max_tokens=1000,
        )

        svg_code = response['choices'][0]['message']['content'].strip()
        if not svg_code.startswith("<svg"):
            raise ValueError("Response from LLM does not appear to be valid SVG.")
        return svg_code

