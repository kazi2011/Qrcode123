import streamlit as st 
from PIL import Image

img = Image.open("Myself.kz.jpg")
st.image(
    img ,
    caption = "Myself Qrcode",
    width = 400 ,
    channels = "RGB"
)
img1 = Image.open("Interview.kz.jpg")
st.image(
    img1 ,
    caption = "Interview Qrcode",
    width = 400 ,
    channels = "RGB"
)
