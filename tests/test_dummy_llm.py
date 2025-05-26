# tests/test_dummy_llm.py

from llms.dummy_llm import DummyLLM


def test_dummy_llm_returns_svg():
    llm = DummyLLM()
    prompt = "smart city"
    svg = llm.generate_icon_svg(prompt)
    assert "<svg" in svg and "</svg>" in svg
    print("[✓] DummyLLM SVG generation test passed.")

