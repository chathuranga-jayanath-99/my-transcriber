import whisper
from gen_files import create_text_files, list_audio_file_names

audio_dir = "./audios"
transcribe_dir = "./transcribes"
audio_ext = ".mp3"

audio_file_names = list_audio_file_names(audio_dir, [audio_ext])
create_text_files(transcribe_dir, audio_file_names)

print("---------------------------------")
print("WELCOME to MY TRANSCRIBER")
print("---------------------------------")
print("\nHere are the audio files available to be transcribed. ")

# list audio file names
for i in range(len(audio_file_names)):
    print(f"{i+1}. {audio_file_names[i]}")

selectd_idx = int(input("Select a file: "))

filename = audio_file_names[selectd_idx-1].split(".")[0]
model = whisper.load_model('base')
result = model.transcribe(f'./{audio_dir}/{filename}.mp3')

with open(f'./{transcribe_dir}/{filename}.txt', 'w') as f:
    f.write(result['text'])
