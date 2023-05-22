from decipher.action import transcribe
import yt_dlp
import os
import shutil
import inquirer
path = './temp'

if not os.path.exists(path):
  os.mkdir(path)

while True:

    os.system('clear')


# Video Download
    links = input("Please type your YouTube Video Link Here and Press Enter : ")
# Rename the Generated SRT File
    file_rename = input("Please input your filename here : ")
    file_rename = os.path.splitext(file_rename)[0] + ".srt"
# Set-default language for transcribe
    language = input("Please Type your transcribe language (Leave it blank to Auto Detect)")

# Clear the Screen

    os.system('clear')

# Asking the Whisper Model

    questions = [
        inquirer.List('model', message='Please Choose your Whisper Model', choices=['tiny.en','tiny','base.en','base','small.en','small','medium.en','medium','large-v1','large-v2','large']),
    ]
# Set Model's Answer

    answers = inquirer.prompt(questions)

    model = answers['model']

    os.system('clear')

# Translate Settings

    questions2 = [
        inquirer.List('translate', message='Do you want to Translate the Video?', choices=['yes', 'no']),
    ]

    answers2 = inquirer.prompt(questions2)

    translate = answers2['translate']

    os.system('clear')

# If User Choose Yes in Translate

    if translate.lower() == "yes":
        translate_to_language = input("Please enter the language you would like to translate to : ")
        print("Please Check the Following Settings is Correct or not")
        print("Video Link : ", links)
        print("File Name : ", file_rename)
        print("language : ", language)
        print("translate? : ", translate)
        print("Output Language : ", translate_to_language)
        
        questions3 = [
                    inquirer.List('continue', message='Is these Options all Correct?', choices=['yes', 'no']),
                ]

        answers3 = inquirer.prompt(questions3)

        loopbreaker = answers3['continue']

        if loopbreaker.lower() == "yes":
            break
        else:
            print('This is just a placeholder LAMO')

# If User Choose No in Translate

    else:
        print("Please Check the Following Settings is Correct or not")
        print("Video Link : ", links)
        print("File Name : ", file_rename)
        print("language : ", language)
        print("translate? : ", translate)
        questions4 = [
                inquirer.List('continue', message='Is these Options all Correct?', choices=['yes', 'no']),
            ]
        answers4 = inquirer.prompt(questions4)

        loopbreaker = answers4['continue']

        if loopbreaker.lower() == "yes":
            break
        else:
            print('This is just a placeholder LAMO')

# Download the YouTube Video

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

# transcribe/Translate The Video

if translate.lower() == 'no':
    input = "./temp/audio.m4a"
    output_dir = "./Generated"
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
elif translate.lower() == 'yes':
    input = "./temp/audio.m4a"
    output_dir = "./Generated"
    task = "translate"
    subtitle_action = "None"

    from decipher.action import transcribe
    import os

    transcribe(
        input, 
        output_dir,
        model,
        translate_to_language if translate_to_language else None,
        task,
        subtitle_action if subtitle_action != "None" else None
    )
else:
    print("How come did you find this text LAMO!")

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
