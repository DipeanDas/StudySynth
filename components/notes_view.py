import streamlit as st

def render_notes(summary):
    with st.container(border=True):
        st.subheader("Notes")
        st.write(summary)