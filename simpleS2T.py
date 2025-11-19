from vosk import Model, KaldiRecognizer
import pyaudio
import json
import os
import sys



MODEL_PATH = r"C:\Users\pcm\Downloads\SMWEB22\vosk-model-small-ru-0.22\\"


model = Model(MODEL_PATH)

SAMPLE_RATE = 16000
CHUNK_SIZE = 4000

rec = KaldiRecognizer(model, SAMPLE_RATE)
rec.SetWords(False)

p = pyaudio.PyAudio()
stream = p.open(
    format=pyaudio.paInt16,
    channels=1,
    rate=SAMPLE_RATE,
    input=True,
    frames_per_buffer=CHUNK_SIZE
)

print("Говорите... (Ctrl+C для выхода)")

while True:
    data = stream.read(CHUNK_SIZE)
    if rec.AcceptWaveform(data):
        result = json.loads(rec.Result())
        if result.get("text"):
            print( result["text"])
    else:
        partial = json.loads(rec.PartialResult())
        if partial.get("partial"):

            print( partial["partial"], end="\r", flush=True)

