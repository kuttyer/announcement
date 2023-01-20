import soundfile
import speech_recognition as sr

path = "./work_dir/"
work_file = "Angol_Udvozlo_456-8856.wav"
data, samplerate = soundfile.read(path+work_file)
soundfile.write('new.wav', data, samplerate, subtype='PCM_24')

filename = "new.wav"

r = sr.Recognizer()
with sr.AudioFile(filename) as source:
    # listen for the data (load audio to memory)
    audio_data = r.record(source)
    # recognize (convert from speech to text)
    text = r.recognize_google(audio_data, language="en-EN")
    print(work_file+":", text)
    text = r.recognize_google(audio_data, language="hu-HU")
    print(work_file + ":", text)
