import speech_recognition as sr
from coloring_terminal import bcolors
import pyttsx3

# walnar = pyttsx3.init()

import gtts
from playsound import playsound

# Returns false if could not get voice
def ai_ask(message, fallback):
  # The user's answer
  response = ""
  r = sr.Recognizer()                 # initialize recognizer
  with sr.Microphone() as source:     # mention source it will be either Microphone or audio files.
    print(f'{bcolors.AI}AI - {message}{bcolors.ENDC}')
    tts = gtts.gTTS(message)
    tts.save('walner.mp3')
    playsound('walner.mp3')
    audio = r.listen(source)        # listen to the source
    # walnar.say(message)
    # walnar.runAndWait()
    try:
        response = r.recognize_google(audio)    # use recognizer to convert our audio into text part.
        print(f'{bcolors.USER}YOU - {response} {bcolors.ENDC}')
    except:
        print("Something didn't work, using fallback")  
        response = fallback
  return response