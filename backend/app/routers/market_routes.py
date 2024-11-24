from fastapi import APIRouter, Response
from app.models.market import MarketAnalysisRequest
from app.services.groq_client import GroqClient

router = APIRouter()
groq_client = GroqClient()

@router.post("/market-analysis")
async def market_analysis(request: MarketAnalysisRequest, response: Response):
    """
    Provides market analysis for the given idea and returns a plain text response.
    """
    prompt = f"""
    Analyze the market for {request.idea}.
    Provide insights on:
    1. Key players
    2. Trends
    3. Challenges
    4. Opportunities
    """
    result = groq_client.query(prompt)
    
    # Return plain text
    response.headers["Content-Type"] = "text/plain"
    return f"Market Analysis for '{request.idea}':\n\n{result}"
