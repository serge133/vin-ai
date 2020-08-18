import speech_recognition as sr     # import the library
from training import train

def ask():
    r = sr.Recognizer()                 # initialize recognizer
    with sr.Microphone() as source:     # mention source it will be either Microphone or audio files.
        print("Speak Anything :")
        audio = r.listen(source)        # listen to the source
        
        try:
            text = r.recognize_google(audio)    # use recognizer to convert our audio into text part.
            print(text)
            if "hello" or "hi" in text:
                print("Hello!")
        except:
            print("Sorry could not recognize your voice")    # In case of voice not recognized  clearly
