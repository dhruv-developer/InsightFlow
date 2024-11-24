# from fastapi import APIRouter
# from app.models.tools import SimplifyRequest
# from app.services.groq_client import GroqClient

# router = APIRouter()
# groq_client = GroqClient()

# @router.post("/fact-check")
# async def fact_check(request: SimplifyRequest):
#     prompt = f"Fact-check this statement and provide references: {request.text}"
#     response = groq_client.query(prompt)
#     return {"verified": True, "references": response}
