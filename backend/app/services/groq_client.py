from langchain_groq import ChatGroq

class GroqClient:
    def __init__(self):
        self.api_key = "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"
        self.model_name = "llama-3.1-70b-versatile"
        self.agent = ChatGroq(
            temperature=0.7,
            groq_api_key=self.api_key,
            model_name=self.model_name
        )

    def query(self, prompt: str) -> str:
        response = self.agent.invoke(prompt)
        return response.content if hasattr(response, "content") else str(response)
