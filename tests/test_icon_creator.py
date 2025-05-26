# tests/test_icon_creator.py

from icon_generator.icon_creator import IconCreator
from llms.dummy_llm import DummyLLM
import os


def test_icon_creator_saves_file():
    creator = IconCreator(llm=DummyLLM())
    prompt = "green energy"
    filename = "test_green_energy"
    svg = creator.generate_icon(prompt, name=filename)

    path = os.path.join("output", f"{filename}.svg")
    assert os.path.exists(path)
    assert "<svg" in svg
    print(f"[✓] Icon saved at {path}")

    # Clean up
    os.remove(path)

