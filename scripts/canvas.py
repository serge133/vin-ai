from credentials import userId, apiKey
import requests
import json
import printing
from datetime import datetime, timedelta
import html2text


def _formatHTML(string):
    return html2text.html2text(string)

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

    showDescription = str(input("Show description [yes/no]: "))

    # f = open('test/course.json', 'w')
    # f.write(str(courses_dict[2]))
    # f.close()

    spring_quarter_course_start = datetime.fromisoformat("2022-03-14T16:09:42")

    for course in courses_dict:
        # ! When printing with description it does not print all the assignments, make them in order at least to see most relevant
        try:
            course_start_date = datetime.fromisoformat(
                course["created_at"][:-1])
            # Only spring quarter courses
            if course_start_date < spring_quarter_course_start:
                continue
            printing.print_good(course["name"], bold=True)
            assignments = requests.get(
                f'https://deanza.instructure.com/api/v1/users/{userId}/courses/{course["id"]}/assignments?access_token={apiKey}'
            )
            assignments_dict = json.loads(assignments.content)
            for assignment in assignments_dict:
                total_ass += 1
                #  Removes last character can not parse the Z (
                date = assignment["due_at"][:-1]
                formatted_date = datetime.fromisoformat(date)
                today = datetime.now()
                localized_date = formatted_date - timedelta(hours=7)
                assDate = localized_date.strftime(
                    '%b %d %A %I:%M:%S %p')

                if today > formatted_date:
                    # Past Assignments
                    past_ass += 1
                    printing.print_bad("\t" + assDate + " (PAST)")
                    if showDescription == 'yes':
                        print(_formatHTML(assignment["description"]))
                else:
                    # Current Assignments
                    still_due += 1
                    printing.print_good(
                        "\t" + assDate + " (STILL DUE)")
                    # printing.print_good(
                    #     "\t\t" + _formatHTML(assignment["description"]))
                    if showDescription == 'yes':
                        print(_formatHTML(assignment["description"]))

        except:

            continue
    printing.ai_speak(f"Total assignments are: {total_ass}", pre="\t")
    printing.ai_speak(f"Past assignments are: {past_ass}", pre="\t")
    printing.ai_speak(f"Current assignments are: {still_due}", pre="\t")
