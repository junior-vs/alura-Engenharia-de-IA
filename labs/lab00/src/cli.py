import argparse
from src.agents.medical_assistant import MedicalAssistant

def run_cli():
    parser = argparse.ArgumentParser(description="Medical Virtual Assistant CLI")
    parser.add_argument("--query", type=str, required=True, help="Query for the assistant")
    args = parser.parse_args()

    agent = MedicalAssistant()
    response = agent.process_query(args.query)
    print(f"Assistant: {response}")

if __name__ == "__main__":
    run_cli()
