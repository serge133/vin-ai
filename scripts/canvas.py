from urllib import response
from credentials import userId, apiKey
from scripts import util
import requests
import json
import printing
from datetime import datetime

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
        f'https://deanza.instructure.com/api/v1/users/{userId}/enrollments?access_token={apiKey}')

    enrollments_dict = json.loads(grades.content)
    # f = open('save.json', 'w')
    # f.write(str(response.content))
    # f.close()
    courses = requests.get(
        f'https://deanza.instructure.com/api/v1/users/{userId}/courses?access_token={apiKey}'
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


def getCalEvents():

    courses = requests.get(
        f'https://deanza.instructure.com/api/v1/users/{userId}/courses?access_token={apiKey}'
    )

    courses_dict = json.loads(courses.content)
    # f = open("save.json", "w")
    # f.write(str(courses.content))
    # f.close()
    total_ass = 0
    still_due = 0
    past_ass = 0

    for course in courses_dict:
        try:
            printing.print_good(course["name"])
            assignments = requests.get(
                f'https://deanza.instructure.com/api/v1/users/{userId}/courses/{course["id"]}/assignments?access_token={apiKey}'
            )
            assignments_dict = json.loads(assignments.content)
            for assignment in assignments_dict:
                total_ass += 1
                date = assignment["due_at"][:-1]
                formatted_date = datetime.fromisoformat(date)
                today = datetime.now()
                assDate = formatted_date.strftime('%b %d %A %I:%M:%S')
                if today > formatted_date:
                    # Past Assignments
                    past_ass += 1
                    printing.print_bad("\t" + assDate + " (PAST)")
                else:
                    # Current Assignments
                    still_due += 1
                    printing.print_good("\t" + assDate + " (STILL DUE)")

        except:

            continue
    printing.ai_speak(f"Total assignments are: {total_ass}", pre="\t")
    printing.ai_speak(f"Past assignments are: {past_ass}", pre="\t")
    printing.ai_speak(f"Current assignments are: {still_due}", pre="\t")
