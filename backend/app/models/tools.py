from pydantic import BaseModel
from typing import List

class FactCheckRequest(BaseModel):
    text: str

class SimplifyRequest(BaseModel):
    text: str

class ThreadSummaryRequest(BaseModel):
    thread: List[str]
