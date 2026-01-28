"""Main application entry point."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.presentation.api.routes import product_routes, recommendation_routes
from src.infrastructure.database.config import init_db

# Initialize database tables
init_db()

# Create FastAPI app
app = FastAPI(
    title="Clean Architecture Product API",
    description="A FastAPI project following Clean Architecture principles",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(product_routes.router, prefix="/api/v1")
app.include_router(recommendation_routes.router, prefix="/api/v1")


@app.get("/")
def health_check():
    """Health check endpoint."""
    return {"status": "ok", "message": "Service is running"}
