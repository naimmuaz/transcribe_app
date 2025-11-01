import whisper

file = '/Users/naimmuaz/Downloads/test.mp3'

model = whisper.load_model("turbo")
result = model.transcribe(file, fp16=False)

# with open("transcribe_file.txt", "w") as f:
#   f.write(result["text"])