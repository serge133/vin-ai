import sqlite3
import util
from functions import OSactions
from coloring_terminal import bcolors

conn = sqlite3.connect('vin.db')
c = conn.cursor()

def new_engine(ask):
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
  # # Calculating Rows
  # points_array = []
  # for row in rows:
  #   points = 0
  #   print(f"MEASURING {row[0]}")
  #   super_keywords=row[1].split(',')
  #   keywords=row[2].split(',')
  #   antikeywords = row[3].split(',')

  #   for super_keyword in super_keywords:
  #     if super_keyword in lowercase_ask:
  #       points+=2
  #       print("++",super_keyword)
        
  #   if points > 0:
  #     for keyword in keywords:
  #       if keyword in lowercase_ask:
  #         points+=1
  #         print('+', keyword)
  #     for antikeyword in antikeywords:
  #       if antikeyword in lowercase_ask:
  #         points-=2
  #         print('--', antikeyword)
  #   print(points)
  #   points_array.append(points)
  # largest_index = util.index_of_largest_element(points_array)
  # matched = rows[largest_index]
  # # Find unmatched keywords
  # matched_superkeywords = matched[1]
  # matched_keywords = matched[2]
  # unmatched_keywords = []
  best_script_match = match()[4]
  print(f'{bcolors.BOLD}script: {best_script_match}{bcolors.ENDC}')
  # print(script)
  # eval(best_script_match + '()')

def train():
  option = str(input('Train me master\n[teach, add script category, reteach, unteach, test, exit]: '))

  def done():
    print('Done.')
    # Commits changes to database
    conn.commit()
    train()

  def select_category():
    c.execute('SELECT * FROM AI')
    categories = c.fetchall()
    index=0
    for script_category in categories:
      print(f'{index}) {script_category[0]}', sep='\n')
      index+=1
    
    selected_category_index = int(input('What Category: '))
    return categories[selected_category_index][4]


  if option == 'teach':
    script_category = select_category()
    print(script_category)
    print('I need keywords, anti keywords, what I say, and execution script')
    name=str(input("What do I do? "))
    super_keywords = str(input("[Super Keywords] This is searched first (sep=,): ")).strip()
    keywords=str(input("[keywords] ({name} are named variables) (*don't copy super kw in here)(sep=,): " )).strip()
    anti_keywords=str(input("[ANTI keywords]These keywords will abort the execution process (sep=,): ")).strip()
    script_function=str(input("Make sure to check with your scripts in ai-actions.py (e.g. move_folder): ")).strip()
  # Creates Table
    ai_entry=(name, super_keywords, keywords, anti_keywords, script_function)
    # c.execute("CREATE TABLE IF NOT EXISTS AI(name TEXT, super_keywords TEXT, keywords TEXT, antikeywords TEXT, script_category TEXT)")
    c.execute(f'''INSERT INTO {script_category}(name, super_keywords, keywords, antikeywords, script_function) VALUES(?, ?, ?, ?, ?)''', ai_entry)

    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    done()
  elif option == 'add script category':
    script_category_name = str(input('Script Category Name: '))
    c.execute(f"CREATE TABLE IF NOT EXISTS {script_category_name}(name TEXT, super_keywords TEXT, keywords TEXT, antikeywords TEXT, script_function TEXT)")
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
    categories = ['name', 'super_keywords', 'keywords', 'antikeywords', 'script_function']
    index=0
    for category in categories:
      print(f'{index}) {category}')
      index+=1
    category_option = int(input('Edit which category: '))
    edit_what = categories[category_option]
    edit=str(input("New edit: ")).strip()
    c.execute(f'UPDATE AI SET {edit_what} = "{edit}" where name = "{name}"')
    done()
  elif option == 'unteach':
    print('Deleting AI entry')
    done()
  elif option == 'test':
    print("Engine VIN")
    ask=str(input('Ask Something: '))
    new_engine(ask)
    done()
  elif option == 'exit':
    c.close()
    print('Have a great day! :)')
  else:
    print("I don't know that option :(")
    done()


train()