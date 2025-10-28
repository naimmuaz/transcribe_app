import whisper

file = "'/Users/naimmuaz/Downloads/STOP WASTING YEARS. 30 DAYS IS ALL IT TAKES.mp3'"

model = whisper.load_model('turbo')
result = model.transcribe(file)
print(result)