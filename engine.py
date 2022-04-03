import sqlite3
from tracemalloc import stop
import util
# being used by sqlite
from scripts import canvas, os
import printing
import time

conn = sqlite3.connect('vin.db')
c = conn.cursor()


def goodbye():
    printing.ai_speak("Have a nice day :)")
    exit()

# script function is unique for querying
# adds unique keywords to the keywords section


def add_unique_keywords(script_function, lowercase_ask_list):
    c.execute(f'SELECT keywords from AI WHERE script_function=?',
              (script_function,))
    # gets just a string of keywords
    keywords = c.fetchall()[0][0]
    for word in lowercase_ask_list:
        if word not in keywords:
            keywords += f',{word}'

    c.execute(
        f'UPDATE AI SET keywords = "{keywords}" WHERE script_function = "{script_function}"')
    conn.commit()


def add_unique_antikeywords(script_function, lowercase_ask_list):
    c.execute(f'SELECT antikeywords from AI WHERE script_function=?',
              (script_function,))
    # gets just a string of keywords
    antikeywords = c.fetchall()[0][0]
    for word in lowercase_ask_list:
        if word not in antikeywords:
            antikeywords += f',{word}'

    c.execute(
        f'UPDATE AI SET antikeywords = "{antikeywords}" WHERE script_function = "{script_function}"')
    conn.commit()


def ai(ask):
    lowercase_ask = ask.lower().strip()
    lowercase_ask_list = lowercase_ask.split(' ')
    potential_scripts = []

    # Algorithm for finding best match
    # This queries every word in the user input to funnel alike scripts
    # There will be duplicates and that is fine
    exceptions = ["a", "the", "in"]
    for word in lowercase_ask_list:
        if word in exceptions or len(word) <= 2:
            continue
        c.execute(
            f'SELECT * from AI where super_keywords LIKE "%{word}%"'
        )
        row = c.fetchall()
        for script in row:
            potential_scripts.append(script)
        # Uncomment code below to increase accuracy but decrease efficiency
        # c.execute(
        #     f'SELECT * from AI where keywords LIKE %{word}%'
        # )
        # row = c.fetchall()
        # for script in row:
        #     potential_scripts.append(script)

    # Remove duplicates
    revised_potential_scripts = list(set(potential_scripts))

    # Keyword algorithm
    def match():
        points_array = []
        for script in revised_potential_scripts:
            points = 0
            super_keywords = script[1]
            keywords = script[2]
            anti_keywords = script[3]
            # tests super keywords first
            for word in lowercase_ask_list:
                if word in exceptions or len(word) <= 2:
                    continue
                if word in super_keywords:
                    points += 2
                if word in keywords:
                    points += 1
                if word in anti_keywords:
                    points -= 2
            points_array.append(points)
        print("Vin Engine: ", points_array)
        largest_index = util.index_of_largest_element(points_array)
        matched = potential_scripts[largest_index]
        return matched

    best_match = revised_potential_scripts[0]

    # Don't use keyword algorithm if there are one or zero scripts
    if len(revised_potential_scripts) > 1:
        best_match = match()
    # The script name
    best_script_match = best_match[4]
    action_name = best_match[0]
    printing.ai_speak(f'Is the action "{action_name}" correct?')
    was_engine_accurate = str(printing.user_input())
    shouldExecute = True
    # Accuracy learning
    if was_engine_accurate == 'yes':
        add_unique_keywords(best_script_match, lowercase_ask_list)
        print("Adding Unique Keywords")
    elif was_engine_accurate == 'no':
        add_unique_antikeywords(best_script_match, lowercase_ask_list)
        print("Adding Unique Antikeywords")
        shouldExecute = False
        printing.ai_speak(
            'How unfortunate, added to antikeywords, I suggest training')
    # Execute Script
    if shouldExecute:
        printing.ai_speak(f'Executing... {action_name}')
        # The script execution
        # ? Can not handle parameters yet
        eval(f'{best_script_match}()')
    else:
        printing.ai_speak('Not executing...')
    printing.ai_speak("What should I do next?")
    user_ask = str(printing.user_input())
    ai(user_ask)

# ! UPDATE


def verbose_ai(ask):
    speed = 2
    printing.print_action("Initializing Testing Protocol... ")
    lowercase_ask = ask.lower().strip()
    lowercase_ask_list = lowercase_ask.split(' ')
    potential_scripts = []

    # Algorithm for finding best match
    # This queries every word in the user input to funnel alike scripts
    # There will be duplicates and that is fine
    exceptions = ["a", "the", "in"]
    # TEST
    try:
        printing.ai_speak("Checking connection to database: vin.db...")
        time.sleep(speed)
        c.execute(
            'SELECT name from AI where super_keywords LIKE "%folder%"'
        )
        testData = c.fetchall()
        for i in range(0, 2):
            printing.print_good(f'test {i}) {testData[i]} success')
    except:
        printing.print_error("Connecting To Database")
        return
    printing.print_good("Database connected SUCCESS")
    time.sleep(speed)
    for word in lowercase_ask_list:
        printing.print_action(
            f'Fetching scripts with super keywords alike to "{word}"')
        if word in exceptions or len(word) <= 2:
            printing.print_eh(f'"{word}" is an exception')
            time.sleep(speed)
            continue
        c.execute(
            f'SELECT * from AI where super_keywords LIKE "%{word}%"'
        )
        time.sleep(speed)
        row = c.fetchall()
        for script in row:
            potential_scripts.append(script)
            time.sleep(speed)
            printing.ai_speak(f"Potential Script Found: {script[0]}")
        # Uncomment code below to increase accuracy but decrease efficiency
        # c.execute(
        #     f'SELECT * from AI where keywords LIKE %{word}%'
        # )
        # row = c.fetchall()
        # for script in row:
        #     potential_scripts.append(script)

    # Remove duplicates
    printing.print_action("Removing duplicates")
    time.sleep(speed)
    revised_potential_scripts = list(set(potential_scripts))
    print("------------------------Match Algorithm----------------------------------")

    # TESTING FUNCTION
    def meter(length):
        bar = ''
        for _ in range(0, length):
            bar += '*'
        return bar

# Keyword algorithm
    def match():
        points_array = []
        for script in revised_potential_scripts:
            points = 0
            super_keywords = script[1]
            keywords = script[2]
            anti_keywords = script[3]
            printing.print_action(f'Assessing script: "{script[0]}"')
            time.sleep(speed)
            for word in lowercase_ask_list:
                printing.ai_speak(f'Assessing word: "{word}"')
                if word in exceptions or len(word) <= 2:
                    printing.print_eh(f'"{word}" is an exception')
                    time.sleep(speed)
                    continue
                if word in super_keywords:
                    points += 2
                    printing.print_good(
                        f'"{word}" matches super keyword in script "{script[0]}" +2', bold=True)
                    time.sleep(speed)
                if word in keywords:
                    points += 1
                    printing.print_good(
                        f'"{word}" matches keyword in script "{script[0]}" +1')
                    time.sleep(speed)
                if word in anti_keywords:
                    points -= 2
                    printing.print_bad(
                        f'"{word}" matches antikeyword in script "{script[0]}" -2')
                    time.sleep(speed)
            print(f'{script[4]}: {meter(points)}')
            time.sleep(speed)
            points_array.append(points)
        print("Vin Engine: ", points_array)
        largest_index = util.index_of_largest_element(points_array)
        matched = potential_scripts[largest_index]
        return matched

    best_match = revised_potential_scripts[0]

    # Don't use keyword algorithm if there are one or zero scripts
    if len(revised_potential_scripts) > 1:
        best_match = match()
    # The script name
    best_script_match = best_match[4]
    action_name = best_match[0]
    printing.ai_speak(f'Is the action "{action_name}" correct?')
    was_engine_accurate = str(printing.user_input())
    # Accuracy learning
    if was_engine_accurate == 'yes':
        add_unique_keywords(best_script_match, lowercase_ask_list)
        print("Adding Unique Keywords")
    elif was_engine_accurate == 'no':
        add_unique_antikeywords(best_script_match, lowercase_ask_list)
        print("Adding Unique Antikeywords")
        printing.ai_speak(
            'How unfortunate, added to antikeywords, I suggest training')
