import sqlite3
import util
from scripts import OSactions
from coloring_terminal import bcolors
from engine import verbose_ai


conn = sqlite3.connect('vin.db')
c = conn.cursor()

def train():
  option = str(input('Train me master\n[teach, add category, edit category, reteach, unteach, test, exit]: '))

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
    # print(script_category)
    print('I need keywords, anti keywords, what I say, and execution script')
    name=str(input("What do I do? "))
    super_keywords = str(input("[Super Keywords] This is searched first (sep=,): ")).strip()
    keywords=str(input("[keywords] *don't copy super kw in here(sep=,): " )).strip()
    anti_keywords=str(input("[ANTI keywords]These keywords will abort the execution process (sep=,): ")).strip()
    script_function=str(input("Make sure to check with your scripts in ai-actions.py (e.g. move_folder): ")).strip()
  # Creates Table
    ai_entry=(name, super_keywords, keywords, anti_keywords, script_function)
    # c.execute("CREATE TABLE IF NOT EXISTS AI(name TEXT, super_keywords TEXT, keywords TEXT, antikeywords TEXT, script_category TEXT)")
    c.execute(f'''INSERT INTO {script_category}(name, super_keywords, keywords, antikeywords, script_function) VALUES(?, ?, ?, ?, ?)''', ai_entry)

    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    done()
  elif option == 'add category':
    script_category = str(input('Script Category: '))
    # Creates a table
    c.execute(f"CREATE TABLE IF NOT EXISTS {script_category}(name TEXT, super_keywords TEXT, keywords TEXT, antikeywords TEXT, script_function TEXT)")
    # Creates an entry in the table of contents (AI)
    name = str(input("Name of Category: "))
    super_keywords = str(input("[Super Keywords] This is searched first (sep=,): ")).strip()
    keywords=str(input("[keywords] *don't copy super kw in here(sep=,): " )).strip()
    anti_keywords=str(input("[ANTI keywords]These keywords will abort the execution process (sep=,): ")).strip()

    entry = (name, super_keywords, keywords, anti_keywords, script_category)
    c.execute(f'''INSERT INTO AI(name, super_keywords, keywords, antikeywords, script_category) VALUES(?, ?, ?, ?, ?)''', entry)
    done()
  elif option == 'edit category':
    c.execute('SELECT name FROM AI')
    rows = c.fetchall()
    index=0
    for entry in rows:
      print(f'{index}) {entry}')
      index+=1
    option = int(input("Option: "))
    name=rows[option][0]
    columns = ['name', 'super_keywords', 'keywords', 'antikeywords']
    index=0
    for column in columns:
      print(f'{index}) {column}')
      index+=1
    category_option = int(input('Edit which category: '))
    edit_what = columns[category_option]
    edit=str(input("New edit: "))
    print(edit_what, edit, name)
    c.execute(f'UPDATE AI SET {edit_what} = "{edit}" WHERE name = "{name}"')
    done()
  elif option == 'reteach':
    print('Editing AI')
    script_category = select_category()

    c.execute(f"SELECT name FROM {script_category}")
    actions = c.fetchall()
    index=0
    for ai_action in actions:
      print(f'{index}) {ai_action}')
      index+=1
    option=int(input("Option: "))
    name=actions[option][0]
    columns = ['name', 'super_keywords', 'keywords', 'antikeywords', 'script_function']
    index=0
    for column in columns:
      print(f'{index}) {column}')
      index+=1
    category_option = int(input('Edit which category: '))
    edit_what = columns[category_option]
    edit=str(input("New edit: ")).strip()
    c.execute(f'UPDATE {script_category} SET {edit_what} = "{edit}" WHERE name = "{name}"')
    done()
  elif option == 'unteach':
    print('Deleting AI entry')
    script_category = select_category()
    c.execute(f'SELECT name FROM {script_category}')
    actions = c.fetchall()
    index=0
    for action in actions:
      print(f'{index}) {action}')
      index+=1
    option = int(input('Option: '))
    name=actions[option][0]
    c.execute(f'DELETE FROM {script_category} WHERE name = "{name}"')
    done()
  elif option == 'test':
    print("Engine VIN")
    ask=str(input('Ask Something: '))
    verbose_ai(ask)
    done()
  elif option == 'exit':
    c.close()
    print('Have a great day! :)')
  else:
    print("I don't know that option :(")
    done()


train()