from PIL import Image
from config import IMAGE_SIZE

def process_images(uploaded_files):
    images = []

    for file in uploaded_files:
        img = Image.open(file)
        img = img.resize(IMAGE_SIZE)
        images.append(img)

    return images