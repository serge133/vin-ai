# import speech_recognition as sr     # import the library
from engine import engine
from speechrecognition import ai_ask

def ask():
    user_ask = ai_ask('What do you want me to do?', '')
    engine(user_ask)