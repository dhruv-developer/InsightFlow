from fastapi import FastAPI
from app.routers import (
    tools_routes,
    sentiment_routes,
    finance_routes,

    translation_routes,
    market_routes,
)

app = FastAPI(
    title="Groq-Powered Backend",
    description="A powerful API backend integrating Groq's LLAMA for AI-driven functionalities.",
    version="1.0.0",
)

# Include routes
app.include_router(tools_routes.router, prefix="/api/v1/tools", tags=["Tools"])
app.include_router(sentiment_routes.router, prefix="/api/v1/sentiment", tags=["Sentiment Analysis"])
app.include_router(finance_routes.router, prefix="/api/v1/finance", tags=["Finance"])
app.include_router(tools_routes.router, prefix="/api/v1/fact-checker", tags=["Fact Checker"])
app.include_router(tools_routes.router, prefix="/api/v1/summarize-thread", tags=["Summarizer"])
app.include_router(translation_routes.router, prefix="/api/v1/translation", tags=["Translation"])
app.include_router(market_routes.router, prefix="/api/v1/market", tags=["Market Analysis"])

@app.get("/")
async def root():
    """
    Root endpoint for the API.
    """
    return {"message": "Welcome to the Groq-Powered Backend API!"}
