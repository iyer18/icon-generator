# src/llms/ollama_llm.py

import subprocess


class OllamaLLM:
    def __init__(self, model="llama3"):
        self.model = model

    def generate_icon_svg(self, prompt: str) -> str:
        full_prompt = (
            "You are an expert SVG icon designer.\n"
            "Return only a flat minimal SVG for the following prompt:\n"
            f"{prompt}"
        )
        result = subprocess.run(
            ["ollama", "run", self.model],
            input=full_prompt,
            text=True,
            capture_output=True
        )
        output = result.stdout.strip()
        start = output.find("<svg")
        end = output.find("</svg>") + len("</svg>")
        return output[start:end].strip()

