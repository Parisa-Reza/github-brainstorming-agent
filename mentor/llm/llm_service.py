
from langchain_google_genai import (
    ChatGoogleGenerativeAI,
)


class LLMService:

    def __init__(self):

        self.llm = (
            ChatGoogleGenerativeAI(
                model="gemini-3.1-flash-lite"
            )
        )

    def get_llm(self):

        return self.llm

