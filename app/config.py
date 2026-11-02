import os
from pathlib import Path
from pydantic import BaseModel

BASE_DIR = Path(__file__).resolve().parent.parent

class AppConfig(BaseModel):
    app_name: str = "ROI & PF Chatbot"
    version: str = "1.0.0"
    host: str = os.getenv("HOST", "127.0.0.1")
    port: int = int(os.getenv("PORT", "8000"))
    debug: bool = os.getenv("DEBUG", "False").lower() in ("true", "1", "yes")
    gemini_api_key: str = os.getenv("GEMINI_API_KEY", "")

config = AppConfig()
