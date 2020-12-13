import speech_recognition as sr
from os import path
from scipy.io import wavfile

def main():
    f_name = 'C:/Users/Emily Liao/Desktop/LING124/finalproject/asr_tts_app/audio_files/all5.wav'

    r = sr.Recognizer()

    def record_audio():
        with sr.AudioFile(f_name) as source:
            audio = r.record(source)
            voice_data = ''
            try:
                voice_data = r.recognize_google(audio)
            except sr.UnknownValueError:
                print('Sorry, I did not get that')
            except sr.RequestError:
                print('Sorry, service is down')
            return voice_data

    voice_data = record_audio()
    with open('output2.txt', 'w') as f: f.write(voice_data)
    return voice_data

if __name__ == '__main__': main() 
