from dotenv import load_dotenv
import os

load_dotenv()

SURREAL_URL = os.getenv("SURREAL_URL")
SURREAL_USERNAME = os.getenv("SURREAL_USERNAME")
SURREAL_PASSWORD = os.getenv("SURREAL_PASSWORD")

SURREAL_NAMESPACE = os.getenv("SURREAL_NAMESPACE")
SURREAL_DATABASE = os.getenv("SURREAL_DATABASE")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")