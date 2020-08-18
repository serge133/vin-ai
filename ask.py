import speech_recognition as sr     # import the library
from engine import new_engine

def ask():
    r = sr.Recognizer()                 # initialize recognizer
    with sr.Microphone() as source:     # mention source it will be either Microphone or audio files.
        print("Speak Anything :")
        audio = r.listen(source)        # listen to the source
        
        # try:
        text = r.recognize_google(audio)    # use recognizer to convert our audio into text part.
        print(text)
        new_engine(str(text))
        # except:
        #     print("Something didn't work")    # In case of voice not recognized  clearly
