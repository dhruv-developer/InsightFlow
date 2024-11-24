from fastapi import APIRouter, Response
from app.models.translation import TranslationRequest
from app.services.groq_client import GroqClient

router = APIRouter()
groq_client = GroqClient()

@router.post("/translate")
async def translate_text(request: TranslationRequest, response: Response):
    """
    Translates the given text to the specified target language.
    """
    prompt = f"Translate the following text to {request.target_language}: {request.text}"
    result = groq_client.query(prompt)
    response.headers["Content-Type"] = "text/plain"
    return f"Original Text:\n{request.text}\n\nTranslated Text ({request.target_language}):\n{result}"
