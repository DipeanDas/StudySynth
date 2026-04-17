import streamlit as st
from PIL import Image
from config import MAX_IMAGES


def render_sidebar():

    st.markdown("## ⚙️ Controls")

    st.write("")

    # ---------------- IMAGE UPLOAD ----------------
    st.markdown("### Upload Notes")

    images = st.file_uploader(
        "Upload up to 3 images",
        type=["png", "jpg", "jpeg"],
        accept_multiple_files=True
    )

    pil_images = []

    if images:
        if len(images) > MAX_IMAGES:
            st.error(f"Please upload a maximum of {MAX_IMAGES} images.")
        else:
            st.markdown("#### 👀 Preview")

            cols = st.columns(len(images))

            for i, img in enumerate(images):
                pil_img = Image.open(img)
                pil_images.append(pil_img)

                with cols[i]:
                    st.image(pil_img, use_container_width=True)

    st.write("---")

    # ---------------- DIFFICULTY ----------------
    st.markdown("### Quiz Difficulty")

    difficulty = st.selectbox(
        "Select level",
        ["Easy", "Medium", "Hard"],
        index=None,
        placeholder="Choose difficulty level"
    )

    st.write("")

    # ---------------- BUTTON ----------------
    pressed = st.button(
        "🚀 Generate Summary & Quiz",
        type="primary",
        use_container_width=True
    )

    return images, difficulty, pressed