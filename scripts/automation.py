from pynput import keyboard, mouse
import time
import printing
from scripts import util
from urllib import request

def openCanvas():
    ms = mouse.Controller()
    kb = keyboard.Controller()
    ms.position = (1659, 95)
    ms.click(mouse.Button.left)
    time.sleep(3.0)
    kb.press(keyboard.Key.backspace)
    kb.release(keyboard.Key.backspace)
    util.type("https://ssoshib.fhda.edu/idp/profile/SAML2/Redirect/SSO?execution=e3s1")
    kb.press(keyboard.Key.enter)
    kb.release(keyboard.Key.enter)
    time.sleep(1.0)
    ms.position = (1376, 399)
    ms.click(mouse.Button.left)
    ms.release(mouse.Button.left)
    kb.type("20482662")
    ms.position = (1374, 448)
    time.sleep(0.5)
    kb.type("g8260Mic")
    ms.position = (1367, 513)
    ms.click(mouse.Button.left)
    ms.release(mouse.Button.left)

    


    # webUrl = request.urlopen("https://ssoshib.fhda.edu/idp/profile/SAML2/Redirect/SSO?execution=e3s1")
    # print(webUrl.getcode())

    # webData = webUrl.read()
    # print(webData)
