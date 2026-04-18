from gtts import gTTS
import io
import re


def clean_text(text: str) -> str:
    # remove markdown + special symbols
    text = re.sub(r"[#*_`~\-()>]", " ", text)
    text = re.sub(r"\s+", " ", text)  # normalize spaces
    return text.strip()


def generate_audio(text):
    cleaned_text = clean_text(text[:800])  # limit + clean

    tts = gTTS(cleaned_text, lang="en", slow=False)

    audio_buffer = io.BytesIO()
    tts.write_to_fp(audio_buffer)
    audio_buffer.seek(0)

    return audio_buffer