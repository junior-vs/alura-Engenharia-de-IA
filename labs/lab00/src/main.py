import sys
import uvicorn
from src.cli import run_cli

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "cli":
        # Remove 'cli' from args so argparse works correctly
        sys.argv.pop(1)
        run_cli()
    else:
        # Default to running the API
        uvicorn.run("src.api:app", host="0.0.0.0", port=8000, reload=True)

if __name__ == "__main__":
    main()
