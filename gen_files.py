import os
import glob

def list_audio_file_names(directory, extensions=[".wav", ".mp3", ".flac"]):
    audio_file_names = []
    
    for ext in extensions:
        audio_files = glob.glob(os.path.join(directory, f"*{ext}"))
        audio_file_names.extend([os.path.basename(file) for file in audio_files])
    return audio_file_names

def create_text_files(directory, filenames):
    for filename in filenames:
        filepath = f"./{directory}/{filename.split('.')[0]}.txt"
        if not os.path.exists(filepath):
            with open(filepath, "w") as file:
                file.write('')
