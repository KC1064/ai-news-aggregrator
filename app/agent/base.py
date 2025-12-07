import os
from abc import ABC
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()


class BaseAgent(ABC):
    def __init__(self, model: str):
        self.client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        self.model = model