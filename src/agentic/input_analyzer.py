# src/agentic/input_analyzer.py

from typing import List
import re

class KeywordExtractor:
    def __init__(self, llm=None):
        self.llm = llm

    def extract_keywords(self, prompt: str) -> List[str]:
        """
        Extracts key visual/icon-related words from a natural language prompt.
        """
        if self.llm:
            try:
                return self._extract_keywords_with_llm(prompt)
            except Exception as e:
                print(f"LLM failed: {e}. Falling back to rule-based.")
        return self._fallback_keywords(prompt)

    def _extract_keywords_with_llm(self, prompt: str) -> List[str]:
        llm_prompt = (
            "Extract 3-6 keywords that can be represented visually as icons "
            f"from the phrase: '{prompt}'. Return them as a comma-separated list."
        )
        response = self.llm.generate(llm_prompt)
        return [word.strip().lower() for word in response.split(",")]

    def _fallback_keywords(self, prompt: str) -> List[str]:
        words = re.findall(r"\w+", prompt.lower())
        # Simple rule-based filtering
        stopwords = {"a", "the", "and", "of", "in", "on", "for", "with", "to", "is"}
        return [word for word in words if word not in stopwords]

