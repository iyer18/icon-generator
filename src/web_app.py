import gradio as gr
from icon_generator.icon_creator import IconCreator
from llms.dummy_llm import DummyLLM
from llms.openai_llm import OpenAILLM
import os

# Prepare output folder
OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)
openai_llm = OpenAILLM()
dummy_llm = DummyLLM()

# Create LLM instances
llm_instances = {
    "Dummy LLM (fast, placeholder)": DummyLLM(),
    "OpenAI GPT (requires API key)": OpenAILLM(),
}

def get_llm(name: str):
    if name == "OpenAI GPT (requires API key)":
        return openai_llm if openai_llm.available else dummy_llm
    elif name == "Dummy LLM":
        return dummy_llm
    else:
        return dummy_llm
def generate_icon(prompt, llm_name, filename):
    if not prompt.strip():
        return "Please enter an icon description.", None

    llm = get_llm(llm_name)
    if llm is None:
        return f"Unknown LLM backend: {llm_name}", None

    creator = IconCreator(llm=llm)
    try:
        svg = creator.generate_icon(prompt, name=filename or None, save=True)
        return svg, svg
    except Exception as e:
        return f"Error: {str(e)}", None


with gr.Blocks() as demo:
    gr.Markdown("# AI Icon Generator")
    with gr.Row():
        prompt_input = gr.Textbox(label="Icon Description", placeholder="e.g. smart city, green energy, space rocket")
        llm_selector = gr.Dropdown(choices=list(llm_instances.keys()), value="Dummy LLM (fast, placeholder)", label="Select LLM Backend")
    filename_input = gr.Textbox(label="Output Filename (without extension, optional)", placeholder="e.g. smart_city_icon")
    generate_btn = gr.Button("Generate Icon")

    output_svg = gr.Textbox(label="Generated SVG Code", lines=15, interactive=False)
    svg_display = gr.HTML(label="Rendered Icon")

    generate_btn.click(
        fn=generate_icon,
        inputs=[prompt_input, llm_selector, filename_input],
        outputs=[output_svg, svg_display]
    )

if __name__ == "__main__":
    demo.launch()

