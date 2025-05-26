# src/llms/huggingface_llm.py

from transformers import pipeline
from typing import Protocol


class HuggingFaceLLM:
    def __init__(self, model_name="tiiuae/falcon-7b-instruct", device=0):
        self.pipeline = pipeline("text-generation", model=model_name, device=device)

    def generate_icon_svg(self, prompt: str) -> str:
        formatted_prompt = (
            "You are an expert SVG icon designer.\n"
            "Given a short concept, return only clean minimal SVG code.\n"
            f"Concept: {prompt}\n\n"
            "SVG:"
        )
        output = self.pipeline(formatted_prompt, max_new_tokens=500)[0]["generated_text"]
        # Extract SVG from response
        start = output.find("<svg")
        end = output.find("</svg>") + len("</svg>")
        return output[start:end].strip()

