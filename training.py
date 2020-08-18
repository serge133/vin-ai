import sqlite3
import util
from functions import OSactions

conn = sqlite3.connect('vin.db')
c = conn.cursor()

def new_engine(ask):
  print("TESTING")
  lowercase_ask = ask.lower()
  ask_array = lowercase_ask.split(' ')
  directional_keywords = ['to', 'from']

  c.execute('SELECT name, super_keywords, keywords, parameters, script_function from AI')
  rows = c.fetchall()
  points_array = []
  # Calculating Rows
  for row in rows:
    points = 0
    print(f"MEASURING {row[0]}")
    super_keywords=row[1].split(',')
    keywords=row[2].split(',')
    for super_keyword in super_keywords:
      if super_keyword in lowercase_ask:
        points+=2
        print("-- ",super_keyword, ' matched!')
        
    if points > 0:
      for keyword in keywords:
        if keyword in lowercase_ask:
          points+=1
          print('- ', keyword, ' matched!')
    points_array.append(points)
  largest_index = util.index_of_largest_element(points_array)
  matched = rows[largest_index]
  # Find unmatched keywords
  matched_superkeywords = matched[1]
  matched_keywords = []
  unmatched_keywords = []
  avoid = ['to', 'from', 'here', 'there', 'in', 'of', 'on', 'the', 'call', 'name']

  for a in ask_array:
    if a not in matched_superkeywords and a not in matched_keywords and a not in avoid:
      unmatched_keywords.append(a)


  parameters_required = matched[3].split(',') # string,number,dest


  # ! This might need to move
  # def name_inference_engine():
  destinations = ['desktop', 'documents', 'downloads']
  print('parameters required', parameters_required)
  func_params = ''
  for parameter in parameters_required:
    print(True)
    if parameter == 'string': 
      func_params+=unmatched_keywords[0] + ','
    elif parameter == 'dest':
      for destination in destinations:
        if destination in ask_array:
          func_params+=destination + ','
      # print('highlights', highlights, sep='\n')
    # More than enough parameters given
    # for delete_banned_char in avoid:
    #   if delete_banned_char in function_parameters:
    #     function_parameters.remove(delete_banned_char)
    # Makes sure we are not messing with keywords
    # highlights = []
    # for a in ask_array:
      # if a not in matched_superkeywords and a not in matched_keywords:
    

  

  # name_inference_engine()
  

  print(matched, ' won')
  print('function parameters: ', func_params)
  # print('unmatched keywords: ', unmatched_keywords)
  script = str(matched[4] + f'("{func_params[:-1]}")')
  # print(script)
  eval(script)

def train():
  option = str(input('Train me master\n[teach, reteach, unteach, test, exit]: '))

  def done():
    print('Done.')
    # Commits changes to database
    conn.commit()
    train()

  if option == 'teach':
    print('I need keywords, anti keywords, what I say, and execution script')
    name=str(input("What do I do? "))
    super_keywords = str(input("[Super Keywords] This is searched first (sep=,): ")).strip()
    keywords=str(input("[keywords] ({name} are named variables) (*don't copy super kw in here)(sep=,): " )).strip()
    anti_keywords=str(input("[ANTI keywords]These keywords will abort the execution process (sep=,): ")).strip()
    parameters=str(input("[Parameters] (format: string,number,dest) (spe=,): ")).strip()
    script_function=str(input("Make sure to check with your scripts in ai-actions.py (e.g. move_folder): ")).strip()
  # Creates Table
    ai_entry=(name, super_keywords, keywords, anti_keywords, parameters, script_function)
    # c.execute("CREATE TABLE IF NOT EXISTS AI(name TEXT, super_keywords TEXT, keywords TEXT, antikeywords TEXT, parameters TEXT, script_function TEXT)")
    c.execute('''INSERT INTO AI(name, super_keywords, keywords, antikeywords, parameters, script_function) VALUES(?, ?, ?, ?, ?, ?)''', ai_entry)

    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    done()
  elif option == 'reteach':
    print('Editing AI')
    c.execute("SELECT name FROM AI")
    all_ai_actions = c.fetchall()
    index=0
    for ai_action in all_ai_actions:
      print(f'{index}) {ai_action}')
      index+=1
    option=int(input("Option: "))
    name=all_ai_actions[option][0]
    categories = ['name', 'super_keywords', 'keywords', 'antikeywords', 'parameters', 'script_function']
    index=0
    for category in categories:
      print(f'{index}) {category}')
      index+=1
    category_option = int(input('Edit which category: '))
    edit_what = categories[category_option]
    edit=str(input("New edit: "))
    c.execute(f'UPDATE AI SET {edit_what} = "{edit}" where name = "{name}"')
    done()
  elif option == 'unteach':
    print('Deleting AI entry')
    done()
  elif option == 'test':
    print("Engine TEST")
    ask=str(input('Ask Something: '))
    new_engine(ask)
    done()
  elif option == 'exit':
    c.close()
    print('Have a great day! :)')
  else:
    print("I don't know that option :(")
    done()