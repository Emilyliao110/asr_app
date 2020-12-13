import speech_recognition as sr
import random
import os
import time
from email.mime import audio

def main():
    r = sr.Recognizer()

    def record_audio():
        with sr.Microphone() as source:
            audio = r.listen(source)
            voice_data = ''
            try:
                voice_data = r.recognize_google(audio)
            except sr.UnknownValueError:
                print('Sorry, I did not get that')
            except sr.RequestError:
                print('Sorry, service is down')
            return voice_data


    def respond(voice_data1):
        if 'exit' in voice_data:
            exit()
            
    time.sleep(1)
    print('How can I help you?')
    
    voice_data = record_audio()
    respond(voice_data)
    with open('output1.txt', 'w') as f: f.write(voice_data)
    return voice_data


if __name__ == '__main__': main()