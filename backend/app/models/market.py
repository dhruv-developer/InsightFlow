from pydantic import BaseModel

class MarketAnalysisRequest(BaseModel):
    idea: str
