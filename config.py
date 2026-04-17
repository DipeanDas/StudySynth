import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

MODEL_NAME = "gemini-3-flash-preview"

MAX_IMAGES = 3
IMAGE_SIZE = (512, 512)
SUMMARY_LIMIT = 150