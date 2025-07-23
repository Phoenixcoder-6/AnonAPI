from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import router

app = FastAPI(
    title="Data Scrambler API",
    description="Scramble, encrypt, and decrypt your text using simple methods.",
    version="1.0.0"
)

# Optional: Allow cross-origin requests (for frontend use)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(router, prefix="/api")  # Add prefix if needed
