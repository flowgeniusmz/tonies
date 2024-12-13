import os
from pytubefix import YouTube
from pytubefix.cli import on_progress
from io import BytesIO
import re


def clean_filename(filename):
    """ Create a clean filename by removing unallowed characters. """
    pattern = r'[^a-zA-Z0-9._\s-]'
    cleaned_name = re.sub(pattern, '_', filename).replace("_ _", "_").replace("__", "_")
    return cleaned_name


def get_video_id(url: str) -> str:
    """ Return the video ID, which is the part after 'v=' """
    return url.split("v=")[-1]


def download_yt_video(url: str, save_folder="videos"):
    """ Downloads the YouTube video and saves it to the specified folder. """
    # Ensure the save folder exists
    os.makedirs(save_folder, exist_ok=True)

    # Initialize YouTube object and select the highest resolution stream
    yt = YouTube(url=url, on_progress_callback=on_progress)
    video_stream = yt.streams.get_highest_resolution()

    # Clean the video title for a safe filename
    cleaned = clean_filename(filename=yt.title)

    # Define the output path
    save_path = os.path.join(save_folder, f"{cleaned}.mp4")

    # Download the video
    print(f"Downloading: {yt.title}")
    video_stream.download(output_path=save_folder, filename=f"{cleaned}.mp4")
    print(f"Video saved to: {save_path}")


# if __name__ == "__main__":
#     video_url = input("Enter the YouTube video URL: ")
#     download_yt_video(video_url)
videoid = get_video_id("https://www.youtube.com/watch?v=t7bQwwqW-Hc")
print(videoid)