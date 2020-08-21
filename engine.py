import sqlite3
import util
from scripts import OSactions
from coloring_terminal import bcolors

conn = sqlite3.connect('vin.db')
c = conn.cursor()



def ai(ask):
  lowercase_ask = ask.lower().strip()
  c.execute('SELECT name, super_keywords, keywords, antikeywords, script_category from AI')
  rows = c.fetchall()
  def match():
    points_array = []
    for row in rows:
      points = 0
      super_keywords=row[1].split(',')
      keywords=row[2].split(',')
      antikeywords = row[3].split(',')
      for super_keyword in super_keywords:
        if super_keyword in lowercase_ask:
          points+=2
          
      if points > 0:
        for keyword in keywords:
          if keyword in lowercase_ask:
            points+=1
        for antikeyword in antikeywords:
          if antikeyword in lowercase_ask:
            points-=2
      points_array.append(points)
    largest_index = util.index_of_largest_element(points_array)
    matched = rows[largest_index]
    return matched
  chosen_category = match()[4]
  c.execute(f'SELECT name, super_keywords, keywords, antikeywords, script_function from {chosen_category}')
  rows = c.fetchall()
  best_script_match = match()[4]
  eval(f'{best_script_match}("{lowercase_ask}")')

def verbose_ai(ask):
  print("TESTING")
  lowercase_ask = ask.lower().strip()

  c.execute('SELECT name, super_keywords, keywords, antikeywords, script_category from AI')
  rows = c.fetchall()
  def match():
    points_array = []
    for row in rows:
      points = 0
      print(f"MEASURING {row[0]}")
      super_keywords=row[1].split(',')
      keywords=row[2].split(',')
      antikeywords = row[3].split(',')

      # print(keywords.count(''))
      # antikeywords.remove('')

      for super_keyword in super_keywords:
        if super_keyword in lowercase_ask:
          points+=2
          print("++",super_keyword)
          
      if points > 0:
        for keyword in keywords:
          if keyword in lowercase_ask:
            points+=1
            print('+', keyword)
        for antikeyword in antikeywords:
          if antikeyword in lowercase_ask:
            points-=2
            print('--', antikeyword)
        print(points)
      points_array.append(points)
    largest_index = util.index_of_largest_element(points_array)
    matched = rows[largest_index]
    return matched
  
  chosen_category = match()[4]
  print(f'{bcolors.BOLD}script category: {chosen_category}{bcolors.ENDC}')

  c.execute(f'SELECT name, super_keywords, keywords, antikeywords, script_function from {chosen_category}')
  rows = c.fetchall()
  best_script_match = match()[4]
  print(f'{bcolors.BOLD}script: {best_script_match}{bcolors.ENDC}')
  # eval(best_script_match + f'("{lowercase_ask}")')
