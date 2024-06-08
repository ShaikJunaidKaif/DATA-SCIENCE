from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# function to load Gemini-pro-vision-model and get response

model = genai.GenerativeModel("gemini-pro-vision")

def get_gemini_response(input, image):
    """
    This function sends the input and image to the model and returns the
    generated response as a string. If the input is not empty, it sends the
    input and the image to the model. If the input is empty, it sends only
    the image to the model.

    Args:
        input (str): The input text to send to the model.
        image (PIL.Image.Image): The image to send to the model.

    Returns:
        str: The generated response from the model.
    """
    if input != "":
        response = model.generate_content([input, image])
    else:
        response = model.generate_content(image)
    return response.text
    
# initialize our streamlit app

st.set_page_config(page_title="Gemini Image Demo")

st.header("Gemini Application")
input = st.text_input("Input Prompt: ", key=input)

uploaded_file = st.file_uploader("Choose an image... ", type=["jpg", "jpeg", "png"])
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit = st.button("Tell me about the image")
# if submit is clicked
if submit:
    response = get_gemini_response(input, image)
    st.subheader("The Response is")
    st.write(response)
