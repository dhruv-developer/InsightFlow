from fastapi import APIRouter, Response
from app.models.sentiment import SentimentRequest, EmotionRequest
from app.services.groq_client import GroqClient

router = APIRouter()
groq_client = GroqClient()

@router.post("/analyze-sentiment")
async def analyze_sentiment(request: SentimentRequest, response: Response):
    """
    Analyze the sentiment of the provided text.
    """
    prompt = f"Analyze the sentiment of this text: {request.text}"
    result = groq_client.query(prompt)
    response.headers["Content-Type"] = "text/plain"
    return f"Sentiment Analysis:\n\n{result}"

@router.post("/emotion-detection")
async def emotion_detection(request: EmotionRequest, response: Response):
    """
    Detect the emotions present in the provided text.
    """
    prompt = f"Detect the emotions in this text: {request.text}"
    result = groq_client.query(prompt)
    response.headers["Content-Type"] = "text/plain"
    return f"Emotion Analysis:\n\n{result}"
