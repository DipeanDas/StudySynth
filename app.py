import streamlit as st

from components.sidebar import render_sidebar
from components.notes_view import render_notes
from components.quiz_view import render_quiz
from components.audio_view import render_audio

from services.ai_service import generate_notes_and_quiz
from services.audio_service import generate_audio

from utils.parser import parse_response
from utils.image_utils import process_images

@st.cache_data
def get_ai_output(images, difficulty):
    return generate_notes_and_quiz(images, difficulty)

st.markdown(
    """
    <style>

    /* Sidebar background */
    section[data-testid="stSidebar"] {
        background-color: #0f172a;
    }

    /* Sidebar text */
    section[data-testid="stSidebar"] * {
        color: #e2e8f0;
    }

    /* Section headers */
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3 {
        color: #ffffff;
        font-weight: 700;
    }

    /* File uploader box */
    section[data-testid="stSidebar"] div[data-testid="stFileUploader"] {
        background-color: #111827;
        border-radius: 10px;
        padding: 10px;
        border: 1px solid #1f2937;
    }

    /* Selectbox */
    section[data-testid="stSidebar"] div[data-baseweb="select"] {
        background-color: #111827;
        border-radius: 8px;
    }

    /* Button */
    section[data-testid="stSidebar"] button {
        background: linear-gradient(90deg, #4F46E5, #06B6D4);
        color: white;
        border-radius: 10px;
        font-weight: 600;
        border: none;
    }

    section[data-testid="stSidebar"] button:hover {
        transform: scale(1.02);
        transition: 0.2s;
    }

    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <h1 style='text-align: center; font-size: 52px; font-weight: 2000; 
    background: linear-gradient(90deg, #4F46E5, #06B6D4);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;'>
    StudySynth
    </h1>
    """,
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align: center; font-size: 24px; color: white;'>"
    "Synthesize your notes into smarter learning"
    "</p>",
    unsafe_allow_html=True
)

st.divider()

# ---------------- SESSION STATE ----------------
if "summary" not in st.session_state:
    st.session_state.summary = None

if "questions" not in st.session_state:
    st.session_state.questions = None

if "generated" not in st.session_state:
    st.session_state.generated = False

if "generate" not in st.session_state:
    st.session_state.generate = False

if "quiz_submitted" not in st.session_state:
    st.session_state.quiz_submitted = False

if "user_answers" not in st.session_state:
    st.session_state.user_answers = {}


# ---------------- SIDEBAR ----------------
with st.sidebar:
    images, difficulty, pressed = render_sidebar()

# trigger generation
if pressed:
    st.session_state.generate = True


# ---------------- GENERATE ----------------
if st.session_state.generate:

    if not images or not difficulty:
        st.error("Please Upload Images and Select Difficulty Level")
        st.session_state.generate = False

    else:
        processed_images = process_images(images)

        with st.spinner("Wait for AI to summarize your notes..."):
            raw = get_ai_output(processed_images, difficulty)

        summary, questions = parse_response(raw)

        # store results
        st.session_state.summary = summary
        st.session_state.questions = questions
        st.session_state.generated = True

        # reset quiz state
        st.session_state.quiz_submitted = False
        st.session_state.user_answers = {}

        # IMPORTANT: stop re-running generation
        st.session_state.generate = False


# ---------------- DISPLAY OUTPUT ----------------
if st.session_state.generated:

    # NOTES    
    render_notes(st.session_state.summary)

    # AUDIO
    with st.spinner("Generating audio from your notes..."):
        audio = generate_audio(st.session_state.summary)

    
    render_audio(audio)

    # QUIZ
    with st.spinner("Creating quiz based on your notes..."):
        st.success("Solve the Quiz!")

    render_quiz(st.session_state.questions)