from google import genai
from dotenv import load_dotenv
import os,io
from gtts import gTTS

load_dotenv()

my_api_key=os.getenv("GEMINI_API_KEY")
client=genai.Client(api_key=my_api_key)

def note_generator(images):
    prompt="""summarize the pictures  in note format at max 100 words, 
    make sure to add necessary markdown to differentiate different section"""
    response=client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[images,prompt]
    )   
    return response.text

def audio_transcription(text):
    speech=gTTS(text, lang="en", slow=False)
    audio_buffer=io.BytesIO()
    speech.write_to_fp(audio_buffer)
    return audio_buffer

def quiz_generator(image,difficulty):
    prompt=f"Generate 3 quizzes based on {difficulty} difficulty level.Make sure to add markdown to differentiate the options.Add correct answers too,after the quiz."
    response=client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[image,prompt]
    )   
    return response.text


