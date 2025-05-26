from setuptools import setup, find_packages

setup(
    name="icon-generator",
    version="0.1.0",
    description="AI Icon Generator using pluggable LLM backends",
    author="Your Name",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "gradio",
        "openai",
    ],
    extras_require={
        "dev": [
            "pytest",
        ],
    },
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)

