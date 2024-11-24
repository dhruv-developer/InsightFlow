from fastapi import APIRouter, Response
from app.models.tools import FactCheckRequest, SimplifyRequest, ThreadSummaryRequest
from app.services.groq_client import GroqClient

router = APIRouter()
groq_client = GroqClient()

@router.post("/fact-check")
async def fact_check(request: FactCheckRequest, response: Response):
    """
    Fact-checks the provided statement and returns verification status and references.
    """
    prompt = f"Fact-check this statement and provide references: {request.text}"
    result = groq_client.query(prompt)
    response.headers["Content-Type"] = "text/plain"
    return f"Fact-Check Result:\n\n{result}"

@router.post("/simplify")
async def simplify_text(request: SimplifyRequest, response: Response):
    """
    Simplifies the provided text for better readability.
    """
    prompt = f"Simplify this text: {request.text}"
    result = groq_client.query(prompt)
    response.headers["Content-Type"] = "text/plain"
    return f"Simplified Text:\n\n{result}"

@router.post("/summarize-thread")
async def summarize_thread(request: ThreadSummaryRequest, response: Response):
    """
    Summarizes the given thread into key points.
    """
    content = " ".join(request.thread)
    prompt = f"Summarize this Twitter thread: {content}"
    result = groq_client.query(prompt)
    response.headers["Content-Type"] = "text/plain"
    return f"Thread Summary:\n\n{result}"
