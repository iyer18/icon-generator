# tests/agentic/test_input_analyzer.py

import unittest
import os
from src.agentic.input_analyzer import KeywordExtractor
from src.llms.dummy_llm import DummyLLM

# Optional real LLM test
try:
    from src.llms.openai_llm import OpenAILLM
except ImportError:
    OpenAILLM = None

class TestKeywordExtractor(unittest.TestCase):
    def test_with_dummy_llm(self):
        extractor = KeywordExtractor(llm=DummyLLM())
        result = extractor.extract_keywords("A smart city with advanced technology and wireless connectivity")
        self.assertIn("city", result)
        self.assertIn("wifi", result)
        self.assertIn("smart", result)
        self.assertIn("signal", result)

    def test_without_llm(self):
        extractor = KeywordExtractor()
        result = extractor.extract_keywords("Smart city with wireless connectivity")
        self.assertIn("smart", result)
        self.assertIn("city", result)
        self.assertIn("wireless", result)
        self.assertIn("connectivity", result)

    @unittest.skipUnless(OpenAILLM and os.getenv("OPENAI_API_KEY"), "OpenAI key not set or module missing")
    def test_with_openai_llm(self):
        extractor = KeywordExtractor(llm=OpenAILLM())
        result = extractor.extract_keywords("Future city with drones, smart traffic, and IoT")
        self.assertIsInstance(result, list)
        self.assertGreaterEqual(len(result), 3)
        for word in result:
            self.assertIsInstance(word, str)

if __name__ == "__main__":
    unittest.main()

