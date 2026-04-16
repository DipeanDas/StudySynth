import streamlit as st
from api_call import note_generator, audio_transcription, quiz_generator 
from PIL import Image

st.title("Note Summary & Quiz Generator")
st.markdown("Upload upto 3 images of your notes to genrate a summary and quiz questions.")
st.divider()

with st.sidebar:
    st.header("Controls")
    #image uploader
    images=st.file_uploader("Upload your notes (max 3 images)", 
                     type=["png", "jpg", "jpeg"], 
                     accept_multiple_files=True)
    pil_image= []
    for img in images:
        pil_image.append(Image.open(img))
    if images:
        if len(images) > 3:
            st.error("Please upload a maximum of 3 images.")
        else:
            col=st.columns(len(images))
            st.subheader("Uploaded Images")
            for i,img in enumerate(images):
                with col[i]:
                    st.image(img)

    #Quiz Difficulty
    s_o=st.selectbox("Select Quiz Difficulty Level", ["Easy", "Medium", "Hard"], index=None,placeholder="Select Difficulty Level")
    # if s_o:
    #     st.markdown(f"You selected **{s_o}** option as difficulty level")
    # else:
    #     st.error("You must select a difficulty level.")
    pressed=st.button("Generate Summary & Quiz", type="primary")

if pressed:
    if not images:
        st.error("You must upload images of your notes.") 
    if not s_o:
        st.error("You must select a difficulty level.")  
    if images and s_o:
        #note
        with st.container(border=True):
            st.subheader("Your Notes")
            with st.spinner("Wait for AI to summarize your notes..."):
                generated_notes=note_generator(pil_image)
                st.markdown(generated_notes)
        #audio
        with st.container(border=True):
            st.subheader("Audio Transcription")
            with st.spinner("Wait for AI to transcribe your notes into audio..."):
                generated_notes= generated_notes.replace("#","")
                generated_notes= generated_notes.replace("*","")
                generated_notes= generated_notes.replace("-","")
                generated_notes= generated_notes.replace("`","")
                generated_notes= generated_notes.replace("(","")
                generated_notes= generated_notes.replace(")","")
                audio_transcript= audio_transcription(generated_notes)
                st.audio(audio_transcript)
        #quiz
        with st.container(border=True):
            st.subheader(f"Quiz : ({s_o}) Difficulty")
            with st.spinner("Wait for AI to generate quiz questions based on your notes..."):
                quizzes= quiz_generator(pil_image,s_o)
                st.markdown(quizzes)
