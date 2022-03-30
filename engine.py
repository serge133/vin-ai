import sqlite3
from tracemalloc import stop
import util
# being used by sqlite
from scripts import os, automation
import printing

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
    c.execute(
        'SELECT name, super_keywords, keywords, antikeywords, script_function from AI')
    rows = c.fetchall()
    # Algorithm for finding best match

    def match():
        points_array = []
        for row in rows:
            points = 0
            super_keywords = row[1]
            keywords = row[2]
            anti_keywords = row[3]
            # tests super keywords first
            for word in lowercase_ask_list:
                if word in super_keywords:
                    points += 2
                if word in keywords:
                    points += 1
                if word in anti_keywords:
                    points -= 2
            points_array.append(points)
        print("Vin Engine: ", points_array)
        largest_index = util.index_of_largest_element(points_array)
        matched = rows[largest_index]
        return matched
    # chosen
    best_match = match()
    # The script name
    best_script_match = best_match[4]
    action_name = best_match[0]
    printing.ai_speak(f'Is the action "{action_name}" correct?')
    was_engine_accurate = str(printing.user_input())
    # // was_engine_accurate = printing.ai.set(f'Is the action {best_match[0]} correct?')
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
    print("TESTING")
    lowercase_ask = ask.lower().strip()

    c.execute(
        'SELECT name, super_keywords, keywords, antikeywords, script_category from AI')
    rows = c.fetchall()

    def match():
        points_array = []
        for row in rows:
            points = 0
            print(f"MEASURING {row[0]}")
            super_keywords = row[1].split(',')
            keywords = row[2].split(',')
            antikeywords = row[3].split(',')

            # print(keywords.count(''))
            # antikeywords.remove('')

            for super_keyword in super_keywords:
                if super_keyword in lowercase_ask:
                    points += 2
                    print("++", super_keyword)

            if points > 0:
                for keyword in keywords:
                    if keyword in lowercase_ask:
                        points += 1
                        print('+', keyword)
                for antikeyword in antikeywords:
                    if antikeyword in lowercase_ask:
                        points -= 2
                        print('--', antikeyword)
                print(points)
            points_array.append(points)
        largest_index = util.index_of_largest_element(points_array)
        matched = rows[largest_index]
        return matched

    chosen_category = match()[4]
    printing.print_action(f'script categroy {chosen_category}')
    c.execute(
        f'SELECT name, super_keywords, keywords, antikeywords, script_function from {chosen_category}')
    rows = c.fetchall()
    best_script_match = match()[4]
    printing.print_action(f'script: {best_script_match}')
    # eval(best_script_match + f'("{lowercase_ask}")')
