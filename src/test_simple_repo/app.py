"""FastAPI application for test-simple-repo."""

from fastapi import FastAPI

from test_simple_repo import __version__
from test_simple_repo.routes import router

app = FastAPI(
    title="test-simple-repo",
    description="Simple test repository",
    version=__version__,
)

app.include_router(router)


@app.get("/health")
async def health_check() -> dict[str, str]:
    """Health check endpoint."""
    return {"status": "healthy", "version": __version__}
