from fastapi import APIRouter, Response
from app.services.groq_client import GroqClient

router = APIRouter()
groq_client = GroqClient()

@router.get("/stock-updates")
async def stock_updates(symbol: str, response: Response):
    """
    Fetch the latest stock price and news for a given symbol.
    """
    prompt = f"Provide the latest stock price and news for {symbol}."
    result = groq_client.query(prompt)
    response.headers["Content-Type"] = "text/plain"
    return f"Stock Updates for {symbol}:\n\n{result}"

@router.get("/crypto-trends")
async def crypto_trends(response: Response):
    """
    Fetch the latest cryptocurrency trends.
    """
    prompt = "List the top cryptocurrency trends this week."
    result = groq_client.query(prompt)
    response.headers["Content-Type"] = "text/plain"
    return f"Crypto Trends:\n\n{result}"

@router.get("/nft-trends")
async def nft_trends(response: Response):
    """
    Fetch the latest trending NFT projects.
    """
    prompt = "What are the top trending NFT projects?"
    result = groq_client.query(prompt)
    response.headers["Content-Type"] = "text/plain"
    return f"NFT Trends:\n\n{result}"
