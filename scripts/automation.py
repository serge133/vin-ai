from pynput import keyboard, mouse
from scripts import util
import requests
import json
import printing

# ? From Canvas


def getGrades():
    # ms = mouse.Controller()
    # kb = keyboard.Controller()
    # ms.position = (1659, 95)
    # ms.click(mouse.Button.left)
    # time.sleep(3.0)
    # kb.press(keyboard.Key.backspace)
    # kb.release(keyboard.Key.backspace)
    # util.type("https://deanza.instructure.com/")

    grades = requests.get(
        'https://deanza.instructure.com/api/v1/users/175330/enrollments?access_token=8683~ipweCk5uzSEnnrn6DdkIDuYoObJ1VaBKyzaEJ22YOKOlo5Wl6eeFjootKqzb4VOJ')

    enrollments_dict = json.loads(grades.content)
    # f = open('save.json', 'w')
    # f.write(str(response.content))
    # f.close()
    courses = requests.get(
        'https://deanza.instructure.com/api/v1/users/175330/courses?access_token=8683~ipweCk5uzSEnnrn6DdkIDuYoObJ1VaBKyzaEJ22YOKOlo5Wl6eeFjootKqzb4VOJ'
    )

    courses_dict = json.loads(courses.content)

    print("\nREPORT CARD")
    for enrollment in enrollments_dict:
        for course in courses_dict:
            if course["id"] == enrollment["course_id"]:
                try:
                    grade = enrollment["grades"]["current_score"]
                    message = f'{course["name"]}: {grade}%'

                    if float(grade) >= 90:
                        printing.print_good(message)
                        printing.ai_speak("This is good :)", pre="\t")
                    elif float(grade) >= 80:
                        printing.print_eh(message)
                        printing.ai_speak("This is eh :\\", pre="\t")
                    else:
                        printing.print_bad(message)
                        printing.ai_speak(
                            "Well you can do a little better than this :(\n", pre="\t")
                except:
                    break
                break
