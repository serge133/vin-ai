from threading import local
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

    class Assignment:
        def __init__(self, date, description):
            self.date = date
            self.description = description

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

    # f = open('test/course.json', 'w')
    # f.write(str(courses_dict[2]))
    # f.close()

    spring_quarter_course_start = datetime.fromisoformat("2022-03-14T16:09:42")
    # saves to a to do list
    output = []
    for course in courses_dict:
        # ! When printing with description it does not print all the assignments, make them in order at least to see most relevant
        try:
            course_start_date = datetime.fromisoformat(
                course["created_at"][:-1])
            # Only spring quarter courses
            if course_start_date < spring_quarter_course_start:
                continue
            printing.print_good(course["name"], bold=True)
            output.append(f'<h1>{course["name"]}</h1>\n\n')
            assignments = requests.get(
                f'https://deanza.instructure.com/api/v1/users/{userId}/courses/{course["id"]}/assignments?access_token={apiKey}'
            )
            assignments_dict = json.loads(assignments.content)
            assignments_array = []
            # process array of assignments
            for assignment in assignments_dict:

                date = assignment["due_at"][:-1]
                formatted_date = datetime.fromisoformat(date)
                # Pacific Time
                localized_date = formatted_date - timedelta(hours=7)

                assignments_array.append(Assignment(
                    date=localized_date, description=assignment["description"]))

            for i in range(1, len(assignments_array)):
                # i is index
                key = assignments_array[i]
                j = i - 1

                while j >= 0 and key.date < assignments_array[j].date:
                    # Move the next element before the previous element
                    assignments_array[j + 1] = assignments_array[j]
                    j -= 1
                assignments_array[j + 1] = key

            for ass in assignments_array:
                total_ass += 1
                # Pacific Time Now
                today = datetime.now() - timedelta(hours=7)
                assDate = ass.date.strftime(
                    '%b %d %A %I:%M:%S %p')
                output.append(f'<h2><strong>{assDate}</strong></h2>\n')
                if today > ass.date:
                    # Past Assignments
                    past_ass += 1
                    printing.print_bad("\t" + assDate + " (PAST)")
                else:
                    # Current Assignments
                    still_due += 1
                    printing.print_good(
                        "\t" + assDate + " (STILL DUE)")
                output.append(
                    str(ass.description))

        except:
            continue
    printing.ai_speak(f"Total assignments are: {total_ass}", pre="\t")
    printing.ai_speak(f"Past assignments are: {past_ass}", pre="\t")
    printing.ai_speak(f"Current assignments are: {still_due}", pre="\t")
    output.append(f"\n<h3>Total assignments are: {total_ass}</h3>\n")
    output.append(f"<h3>Past assignments are: {past_ass}</h3>\n")
    output.append(f"<h2>Current assignments are: {still_due}</h2>\n")
    # ! Discussions are not here yet
    output_string = '\n'.join(output)
    f = open("Todo.html", "w")
    f.write(output_string)
    f.close()
    printing.ai_speak("saved :)")
