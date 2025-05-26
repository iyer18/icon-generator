# src/icon_generator/icon_creator.py

import os
from datetime import datetime
from typing import Optional
from llms.openai_llm import OpenAILLM  # Default; swap with DummyLLM or HuggingFaceLLM
# from llms.dummy_llm import DummyLLM
# from llms.ollama_llm import OllamaLLM

OUTPUT_DIR = "output"


class IconCreator:
    def __init__(self, llm=None):
        self.llm = llm or OpenAILLM()

    def generate_icon(self, prompt: str, name: Optional[str] = None, save: bool = True) -> str:
        svg = self.llm.generate_icon_svg(prompt)

        if save:
            os.makedirs(OUTPUT_DIR, exist_ok=True)
            filename = name or self._generate_filename(prompt)
            filepath = os.path.join(OUTPUT_DIR, f"{filename}.svg")
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(svg)
            print(f"[✓] Saved: {filepath}")

        return svg

    def _generate_filename(self, prompt: str) -> str:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        safe_prompt = "_".join(prompt.lower().split())[:30]
        return f"{safe_prompt}_{timestamp}"

