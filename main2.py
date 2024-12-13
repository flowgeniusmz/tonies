from pydub import AudioSegment
import os

video_paths = ["videos/Me Too.mp4","videos/Business.mp4","videos/Older.mp4","videos/Bar Song.mp4"]
for video_path in video_paths:
    audio = AudioSegment.from_file(video_path, format="mp4")
    name = os.path.splittext(video_path[0])
    print(name)
    audio_path = 'songs/' + name + '.mp3'
    
    print(audio_path)

