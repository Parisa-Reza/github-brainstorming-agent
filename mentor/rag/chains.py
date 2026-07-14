from langchain_google_genai import ChatGoogleGenerativeAI

from mentor.config import (
    GEMINI_API_KEY,
)


def get_llm():

    return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=GEMINI_API_KEY,
        temperature=0,
    )