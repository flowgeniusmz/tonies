from pytube import YouTube
from pydub import AudioSegment
import os

#urls = ["https://www.youtube.com/watch?v=wFnYq2pMDbs","https://www.youtube.com/watch?v=ru0K8uYEZWw", "https://www.youtube.com/watch?v=q0hyYWKXF0Q","https://www.youtube.com/watch?v=Pz2t-yJIp2Q","https://www.youtube.com/watch?v=XqZsoesa55w","https://www.youtube.com/watch?v=dIl8imdPrDE","https://www.youtube.com/watch?v=-ipRfLf79WU"]

#url =  "https://www.youtube.com/watch?v=BHcFQ9gaMF4"

urls = ["https://www.youtube.com/watch?v=pOznx1KLN7U", "https://www.youtube.com/watch?v=AWFQx0gGXjs", "https://www.youtube.com/watch?v=t7bQwwqW-Hc", "https://www.youtube.com/watch?v=fA9RBdts7h4", "https://www.youtube.com/watch?v=wJS9eb6_o00", "https://www.youtube.com/watch?v=78S0ROEWEQY", "https://www.youtube.com/watch?v=MJV4vjlziNI"]


def get_song(url):
    yt = YouTube(url)
    audio_stream = yt.streams.filter(only_audio=True).first()

    # Download the audio file
    audio_file_path = audio_stream.download()

    # Load the downloaded audio file with pydub (assuming it's an mp4 audio file)
    audio = AudioSegment.from_file(audio_file_path, format="mp4")

    # Define the path for the mp3 file
    mp3_file_path = 'songs/' + yt.title + '.mp3'

    # Export the audio to mp3
    audio.export(mp3_file_path, format="mp3")

    # Optionally, delete the original download to save space
    os.remove(audio_file_path)

    print(f"Downloaded and converted {yt.title} to MP3.")

for url in urls:    
    get_song(url)
