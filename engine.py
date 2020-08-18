import sqlite3
import util
from functions import OSactions

conn = sqlite3.connect('vin.db')
c = conn.cursor()

def new_engine(ask):
  lowercase_ask = ask.lower()
  ask_array = lowercase_ask.split(' ')
  directional_keywords = ['to', 'from']

  c.execute('SELECT name, super_keywords, keywords, parameters, script_function from AI')
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
  matched_superkeywords = matched[1]
  matched_keywords = []
  unmatched_keywords = []
  avoid = ['to', 'from', 'here', 'there', 'in', 'of', 'on', 'the', 'call', 'name']

  for a in ask_array:
    if a not in matched_superkeywords and a not in matched_keywords and a not in avoid:
      unmatched_keywords.append(a)


  parameters_required = matched[3].split(',') # string,number,dest
  destinations = ['desktop', 'documents', 'downloads']
  func_params = ''
  for parameter in parameters_required:
    if parameter == 'string': 
      func_params+=unmatched_keywords[0] + ','
    elif parameter == 'dest':
      for destination in destinations:
        if destination in ask_array:
          func_params+=destination + ','

  script = str(matched[4] + f'("{func_params[:-1]}")')
  eval(script)
