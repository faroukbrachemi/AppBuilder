# MiniAppBuilder — Automatic Mini-App Generator

This project is an **agentic AI system** that can plan, architect, and generate complete mini web applications from a single natural-language prompt. It uses **LangGraph**, **LangChain**, and an LLM to coordinate multiple agents (Planner, Architect, Coder) and produce a fully structured project folder with ready-to-run code.



https://github.com/user-attachments/assets/1128eebe-0b64-411e-8d6b-a2b3847a0901


## System Architecture

The system follows a multi-agent pipeline:

### **📝 Planner Agent**
Converts a user prompt into a structured high-level plan.

### **🧩 Architect Agent**
Breaks the plan into technical steps and file-level tasks.

### **💻 Coder Agent**
Uses tools to automatically create the project files.

<div style="text-align: center;">
    <img src="graphics/system_workflow.png" alt="System Architecture" width="90%"/>
</div>

## 📁 Project Structure

```
AppBuilder/
│
├── main.py                 # Entry point of the application
├── pyproject.toml          # Project dependencies & config
├── uv.lock                 # Lockfile for reproducible env
│
├── agent/                  
│   ├── graph.py            # LangGraph workflow
│   ├── prompts.py          # Prompt templates
│   ├── states.py           # State definitions
│   └── tools.py            # Custom tools (read/write files, etc.)
│
└── generated_project/      # Auto-generated app output (created at runtime)
```

## 🚀 Getting Started

### **Prerequisites**
- Python 3.10+
- `uv` for environment & dependency management
- An LLM API key (e.g., **Groq**, OpenAI, or any provider supported by LangChain)

## 🛠️ Installation

1. **Clone the repository**
```bash
git clone https://github.com/faroukbrachemi/AppBuilder.git
cd AppBuilder
```

2. **Set up the environment**
```bash
uv init
uv sync
```

3. **Activate the virtual environment**
```bash
source .venv/bin/activate
```

4. **Copy the sample file and add your API key**
```bash
cp .sample_env .env
```

5. **Run the project**
```bash
python main.py
```

## 🧪 **Example Prompts**

- **To-Do List App**: Create a beautiful to-do list application using HTML, CSS, and JavaScript.  
- **Calculator App**: Create a simple calculator web application using HTML, CSS, and JavaScript.  
- **Weather App**: Generate a small weather app that shows the current weather using HTML, CSS, and JavaScript.  
- **Quiz App**: Create a multiple-choice quiz app using HTML, CSS, and JavaScript.  
- **Note-Taking App**: Build a simple note-taking app using HTML, CSS, and JavaScript.  

## 📌 **Notes**
- Each run generates a fully contained project folder with all required files.  
- If you want to generate another project you have to delete the previous one.
