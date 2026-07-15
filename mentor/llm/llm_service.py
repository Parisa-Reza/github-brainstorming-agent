from langchain_google_genai import (
    ChatGoogleGenerativeAI,
)


class LLMService:

    def __init__(self):

        self.llm = (
            ChatGoogleGenerativeAI(
                model="gemini-2.5-flash"
            )
        )

    def generate(
        self,
        prompt: str,
    ):

        response = self.llm.invoke(
            prompt
        )

        return response.content