
import streamlit as st
from pytube import YouTube


# Titulo da aplicação
st.title("YouTube Video DOwnloader")
# Subtitulo da aplicação
st.subheader("Enter ther URL:")
# variavel que recebera o texto do link para download
url = st.text_input(label="URL")

yt = YouTube(url)

print(yt.streams)
