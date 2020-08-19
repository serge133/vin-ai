import sqlite3
import util
from functions import OSactions

conn = sqlite3.connect('vin.db')
c = conn.cursor()

def engine(ask):
  lowercase_ask = ask.lower()
  ask_array = lowercase_ask.split(' ')

  c.execute('SELECT name, super_keywords, keywords, script_function from AI')
  rows = c.fetchall()
  points_array = []
  # Calculating Rows
  for row in rows:
    points = 0
    super_keywords=row[1].split(',')
    keywords=row[2].split(',')

    for super_keyword in super_keywords:
      if super_keyword in lowercase_ask:
        points+=2
        
    if points > 0:
      for keyword in keywords:
        if keyword in lowercase_ask:
          points+=1

    points_array.append(points)
  largest_index = util.index_of_largest_element(points_array)
  matched = rows[largest_index]
  # Find unmatched keywords
  matched_superkeywords = matched[1]
  matched_keywords = []
  unmatched_keywords = []
  

  for a in ask_array:
    if a not in matched_superkeywords and a not in matched_keywords:
      unmatched_keywords.append(a)
  
  script = str(matched[3] + '()')
  print(script)
  eval(script)