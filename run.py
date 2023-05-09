from decipher.action import transcribe
import yt_dlp
import os

path = './.tmp'

if not os.path.exists(path):
  os.mkdir(path)

links = input("Please type your YouTube Video Link Here and Press Enter : ")
name = input("Please type your SRT file name Here and Press Enter : ")

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'aac',
        'preferredquality': '192',
    }],
        'outtmpl': './.tmp/audio',
}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([links])


input = "./.tmp/audio.m4a"
output_dir = "./{name}"
model = "medium"
language = ""
task = "transcribe"
subtitle_action = "None"

from decipher.action import transcribe
import os

transcribe(
    input, 
    output_dir,
    model,
    language if language else None,
    task,
    subtitle_action if subtitle_action != "None" else None
)
