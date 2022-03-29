from pynput import keyboard
import time

def type(sentence):
    kb = keyboard.Controller()
    kb.type(sentence)
    # for letter in sentence:
    #     print(letter)
    #     time.sleep(0.01)
    #     kb.press(letter)
    #     kb.release(letter)