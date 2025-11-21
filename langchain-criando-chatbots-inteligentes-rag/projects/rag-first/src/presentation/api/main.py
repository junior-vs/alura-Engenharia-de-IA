"""Main entry point for the FastAPI application."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""
    app = FastAPI(
        title="RAG-First API",
        description="A RAG-based application following Clean Architecture",
        version="0.1.0",
    )

    # Add CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.get("/")
    async def root() -> dict[str, str]:
        """Root endpoint."""
        return {"message": "Welcome to RAG-First API"}

    @app.get("/health")
    async def health() -> dict[str, str]:
        """Health check endpoint."""
        return {"status": "healthy"}

    return app


app = create_app()


def start_server() -> None:
    """Start the uvicorn server."""
    import uvicorn
    uvicorn.run("src.presentation.api.main:app", host="0.0.0.0", port=8000, reload=True)


if __name__ == "__main__":
    start_server()
