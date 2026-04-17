import streamlit as st

def render_audio(audio_buffer):
    with st.container(border=True):
        st.subheader("Audio")
        st.audio(audio_buffer)