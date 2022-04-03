from pytube import YouTube
import streamlit as st
import datetime
import os


# Titulo da aplicação
st.title("YouTube Video Downloader")
# Subtitulo da aplicação
st.subheader("Enter ther URL:")
# variavel que recebera o texto do link para download
url = st.text_input(label='URL')
# https://www.youtube.com/watch?v=XXYlFuWEuKI
if url != '':
    yt = YouTube(url)
    st.image(yt.thumbnail_url, width=300)
    st.subheader(f'''
    {yt.title}
    Duration: {datetime.timedelta(minutes=yt.length)} minutes
    Views: {yt.views}
    
    ''')

    video = yt.streams
    if len(video) > 0:
        downloaded = False
        download_audio = False

        download_video = st.button("Download Video")
        download_audio = st.button("Download Audio Only")

        for r in video:
            st.text(f'Size: {r.filesize/1000000:.2f}mb')
            st.text(f"Resolition: {r.resolution}")
            st.text(f'FPS: {r.fps}')
            st.text(f'Tipo: {r.mime_type}')

            st.text("\n")

        if download_video:
            #video.filter(resolution=r.resolution, mime_type=r.mime_type, itag=r.itag.download())
            print(r.itag)
            downloaded = True

        if download_audio:
            video.filter(type='audio').first().download()
            downloaded = True
        if downloaded:
            st.success("Download Complete")
else:
    st.text("Please enter a valid URL")


'''
[
    <Stream: itag="17" mime_type="video/3gpp" res="144p" fps="8fps" vcodec="mp4v.20.3" acodec="mp4a.40.2" progressive="True" type="video">,
<Stream: itag="18" mime_type="video/mp4" res="360p" fps="30fps" vcodec="avc1.42001E" acodec="mp4a.40.2" progressive="True" type="video">,
<Stream: itag="22" mime_type="video/mp4" res="720p" fps="30fps" vcodec="avc1.64001F" acodec="mp4a.40.2" progressive="True" type="video">,
<Stream: itag="299" mime_type="video/mp4" res="1080p" fps="60fps" vcodec="avc1.64002a" progressive="False" type="video">,
<Stream: itag="303" mime_type="video/webm" res="1080p" fps="60fps" vcodec="vp9" progressive="False" type="video">,
<Stream: itag="298" mime_type="video/mp4" res="720p" fps="60fps" vcodec="avc1.4d4020" progressive="False" type="video">,
<Stream: itag="302" mime_type="video/webm" res="720p" fps="60fps" vcodec="vp9" progressive="False" type="video">,
<Stream: itag="135" mime_type="video/mp4" res="480p" fps="30fps" vcodec="avc1.4d401f" progressive="False" type="video">,
<Stream: itag="244" mime_type="video/webm" res="480p" fps="30fps" vcodec="vp9" progressive="False" type="video">,
<Stream: itag="134" mime_type="video/mp4" res="360p" fps="30fps" vcodec="avc1.4d401e" progressive="False" type="video">,
<Stream: itag="243" mime_type="video/webm" res="360p" fps="30fps" vcodec="vp9" progressive="False" type="video">,
<Stream: itag="133" mime_type="video/mp4" res="240p" fps="30fps" vcodec="avc1.4d4015" progressive="False" type="video">,
<Stream: itag="242" mime_type="video/webm" res="240p" fps="30fps" vcodec="vp9" progressive="False" type="video">,
<Stream: itag="160" mime_type="video/mp4" res="144p" fps="30fps" vcodec="avc1.4d400c" progressive="False" type="video">,
<Stream: itag="278" mime_type="video/webm" res="144p" fps="30fps" vcodec="vp9" progressive="False" type="video">,
<Stream: itag="139" mime_type="audio/mp4" abr="48kbps" acodec="mp4a.40.5" progressive="False" type="audio">,
<Stream: itag="140" mime_type="audio/mp4" abr="128kbps" acodec="mp4a.40.2" progressive="False" type="audio">,
<Stream: itag="249" mime_type="audio/webm" abr="50kbps" acodec="opus" progressive="False" type="audio">,
<Stream: itag="250" mime_type="audio/webm" abr="70kbps" acodec="opus" progressive="False" type="audio">,
<Stream: itag="251" mime_type="audio/webm" abr="160kbps" acodec="opus" progressive="False" type="audio">
]
'''
