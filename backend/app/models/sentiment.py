from pydantic import BaseModel

class SentimentRequest(BaseModel):
    text: str

class EmotionRequest(BaseModel):
    text: str
