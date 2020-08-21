import engine
# from speechrecognition import ai_ask
import printing

# user_ask = ai_ask('What do you want me to do?', '')
printing.ai_speak("What do you want to do?")
user_ask = str(printing.user_input())
engine.ai(user_ask)