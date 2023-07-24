import speech_recognition as sr
import os
import winsound
import pyaudio
import wave
seconds = 11
start = True


def recsec():
    global seconds
    seconds = int(input('How many seconds do you want to record?'))
    if seconds >= 20:
        print('Invalid number, Higher than 20 seconds is forbidden')
        recsec()


recsec()
p = pyaudio.PyAudio()
winsound.Beep(2000, 175)
stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
frames = []
try:
    while True:
        for i in range(seconds * 45):
            data = stream.read(1024)
            frames.append(data)
        break
except KeyboardInterrupt:
    pass
stream.stop_stream()
stream.close()
p.terminate()
sound_file = wave.open("output.wav", "wb")
sound_file.setnchannels(1)
sound_file.setsampwidth(p.get_sample_size(pyaudio.paInt16))
sound_file.setframerate(44100)
sound_file.writeframes(b''.join(frames))
sound_file.close()
filename = "output.wav"
r = sr.Recognizer()
with sr.AudioFile(filename) as source:
    # listen for the data (load audio to memory)
    audio_data = r.record(source)
    # recognize (convert from speech to text)
    UInput = input('which language do you want?')
    if UInput == 'arabic':
        lang = 'ar-AR'
    else:
        lang = 'en-EN'
    text = r.recognize_google(audio_data, language=lang)
    print(text)
os.remove("output.wav")
