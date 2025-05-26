# src/llms/dummy_llm.py

class DummyLLM:
    def __init__(self):
        pass

    def generate_icon_svg(self, prompt: str) -> str:
        # Return a hardcoded SVG for testing purposes
        return f"""
        <svg width="100" height="100" xmlns="http://www.w3.org/2000/svg">
            <rect width="100" height="100" fill="lightgray" />
            <text x="10" y="55" font-size="14" fill="black">🧠 {prompt}</text>
        </svg>
        """

