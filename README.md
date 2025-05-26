# AI Icon Generator

A Python tool to generate SVG icons from text prompts using pluggable LLM backends.  
Supports OpenAI GPT and a dummy local LLM for quick testing.

---

## Features

- Modular LLM abstraction for flexible backend switching  
- Generates SVG icon code from natural language prompts  
- Simple web UI with Gradio for interactive icon creation and preview  
- Save generated SVG icons with custom names  
- Comes with sample tests for easy development

---

## Project Structure

icon-generator/
├── LICENSE
├── README.md
├── data/
├── docs/
├── output/ # generated SVG files saved here
├── requirements.txt
├── setup.py
├── src/
│ ├── icon_generator/
│ │ └── icon_creator.py
│ └── llms/
│ ├── dummy_llm.py
│ └── openai_llm.py
├── tests/
│ ├── test_dummy_llm.py
│ └── test_icon_creator.py


## Setup

### Prerequisites

- Python 3.7+  
- (Optional) OpenAI API key in your environment as `OPENAI_API_KEY` if using OpenAI backend  

### Install dependencies

pip install -r requirements.txt


## Usage

###Run the Web App
python3 src/web_app.py
Open the URL printed by Gradio (usually http://127.0.0.1:7860) to start generating icons

###Generate Icons in Python (example)
from icon_generator.icon_creator import IconCreator
from llms.dummy_llm import DummyLLM

creator = IconCreator(llm=DummyLLM())
svg_code = creator.generate_icon("smart city", name="smart_city_icon")
print(svg_code)

## Running Tests

You can run the test files directly with:

PYTHONPATH=src python3 tests/test_dummy_llm.py
PYTHONPATH=src python3 tests/test_icon_creator.py

Or using pytest (recommended):
pip install pytest
PYTHONPATH=src pytest tests/

## Environment Variables

OPENAI_API_KEY: Your OpenAI API key for the OpenAI LLM backend.



