import streamlit as st
import yt_dlp
from io import BytesIO
import os
import requests
from pytube import YouTube, StreamQuery
import base64
import os
from pydub import AudioSegment

#urls = ["https://www.youtube.com/watch?v=pOznx1KLN7U", "https://www.youtube.com/watch?v=AWFQx0gGXjs", "https://www.youtube.com/watch?v=t7bQwwqW-Hc", "https://www.youtube.com/watch?v=fA9RBdts7h4", "https://www.youtube.com/watch?v=wJS9eb6_o00", "https://www.youtube.com/watch?v=78S0ROEWEQY", "https://www.youtube.com/watch?v=MJV4vjlziNI"]

url1 = "https://www.youtube.com/watch?v=pOznx1KLN7U"
url2 = "https://www.youtube.com/watch?v=AWFQx0gGXjs"
url3 = "https://www.youtube.com/watch?v=t7bQwwqW-Hc" #
url4 = "https://www.youtube.com/watch?v=fA9RBdts7h4"#
url5 = "https://www.youtube.com/watch?v=wJS9eb6_o00"
url6 = "https://www.youtube.com/watch?v=78S0ROEWEQY"#
url7 = "https://www.youtube.com/watch?v=MJV4vjlziNI"

def convert_to_mp3(link: str):
    temp_file = BytesIO()  # Temporary in-memory file

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': 'temp_audio.%(ext)s',  # Save to a temporary file
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # Extract and download audio
        info_dict = ydl.extract_info(link, download=True)
        mp3_title = info_dict.get('title', 'audio') + ".mp3"

        # Read the downloaded file into memory
        with open("temp_audio.mp3", "rb") as audio_file:
            temp_file.write(audio_file.read())

    # Clean up temporary file
    os.remove("temp_audio.mp3")

    temp_file.seek(0)  # Reset buffer position for downloading
    return temp_file, mp3_title

convert_to_mp3(link=url1)