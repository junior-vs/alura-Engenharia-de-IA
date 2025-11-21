# Medical Virtual Assistant

## Overview
This project is a medical virtual assistant designed to assist with clinical decisions, answer doctor's questions, and suggest procedures based on internal protocols. It uses a fine-tuned LLM and RAG (Retrieval-Augmented Generation) to provide accurate and context-aware responses.

## Features
- **Fine-tuned LLM**: Trained on internal hospital protocols and data.
- **RAG Pipeline**: Retrieves relevant information from medical documents and patient records.
- **LangChain & LangGraph**: Orchestrates the assistant's logic and decision flows.
- **Guardrails**: Ensures safety and compliance in responses.
- **Interfaces**: CLI and RESTful API (FastAPI).

## Project Structure
```
.
├── config/             # Configuration settings
├── data/               # Data storage (placeholder)
├── docs/               # Documentation
├── notebooks/          # Experimentation notebooks
├── src/                # Source code
│   ├── agents/         # Agent logic
│   ├── loaders/        # Document loaders
│   ├── rag/            # RAG pipeline components
│   ├── utils/          # Utility functions (logging, security)
│   ├── api.py          # FastAPI application
│   ├── cli.py          # CLI entry point
│   └── main.py         # Main entry point
├── tests/              # Unit and integration tests
├── .gitignore
├── pyproject.toml
├── README.md
└── requirements.txt
```

## Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd <repository_name>
    ```

2.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies:**
    Using `uv` (recommended):
    ```bash
    uv sync
    ```
    
    Or using `pip`:
    ```bash
    pip install -e .[dev]
    ```

## Configuration

1.  **Environment Variables:**
    Create a `.env` file in the root directory and add your API keys and configuration:
    ```env
    OPENAI_API_KEY=your_key_here
    # Add other keys as needed
    ```

## Usage

### Running the API
```bash
uvicorn src.api:app --reload
```

### Running the CLI
```bash
python src/main.py cli --query "Patient symptoms..."
```

## Testing
Run tests using pytest:
```bash
pytest
```
