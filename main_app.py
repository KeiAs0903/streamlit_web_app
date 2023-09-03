import streamlit as st
from PIL import Image

st.title('試作アプリ')
st.caption('これは試作アプリです')

image = Image.open('./data/フライボード.png')
st.image(image, width=200)
