from google import genai
from config import GEMINI_API_KEY, MODEL_NAME

client = genai.Client(api_key=GEMINI_API_KEY)

def generate_notes_and_quiz(images, difficulty):
    prompt = f"""
Summarize in note format in <=150 words. 
Make sure to add necessary markdown to differentiate different section
Then generate 3 {difficulty} MCQs.
Format:
SUMMARY:
...

QUIZ:
Q1|question
a) option

ANS: a
"""
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=images + [prompt]
    )

    return response.text