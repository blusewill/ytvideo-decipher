from decipher.action import transcribe
import yt_dlp
import os
import shutil
path = './temp'

if not os.path.exists(path):
  os.mkdir(path)

links = input("Please type your YouTube Video Link Here and Press Enter : ")
file_rename = input("Please input your filename here : ")
file_rename = os.path.splitext(file_rename)[0] + ".srt"

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'aac',
        'preferredquality': '192',
    }],
        'outtmpl': './temp/audio',
}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([links])


input = "./temp/audio.m4a"
output_dir = "./Generated"
model = "small"
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

# Removing The Temp Audio Files

directory_path = os.path.join(os.getcwd(), '../temp')

os.path.exists(directory_path)
shutil.rmtree(directory_path)


# Rename the SRT File

current_file_path = './audio.srt'
directory_path = os.path.dirname(current_file_path)
file_name = os.path.basename(current_file_path)
new_file_path = os.path.join(directory_path, file_rename)
os.rename(current_file_path, new_file_path)
