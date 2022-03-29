import sqlite3
from uuid import uuid4
import util
from scripts import OSactions
from coloring_terminal import bcolors
from engine import verbose_ai

conn = sqlite3.connect('vin.db')
c = conn.cursor()

def train():
  option = str(input('[teach, edit, reteach, unteach, test, exit]: '))

  # Commits changes to database
  def done():
    print('Done.')
    conn.commit()
    # activates loop until exit
    train() 

  if option == 'teach':
    print('I need keywords, anti keywords, what I say, and execution script')
    name=str(input("What do I do? "))
    super_keywords = str(input("[Super Keywords] This is searched first (sep=,): ")).strip()
    anti_keywords=str(input("[ANTI keywords]These keywords will abort the execution process (sep=,): ")).strip()
    script_function=str(input("Make sure to check with your scripts in ai-actions.py (e.g. move_folder): ")).strip()
  # Creates Table
  # keywords is empty this is handled by the engine
    ai_entry=(name, super_keywords, '', anti_keywords, script_function)
    # if the table does not exist
    c.execute("CREATE TABLE IF NOT EXISTS AI(name TEXT, super_keywords TEXT, keywords TEXT, antikeywords TEXT, script_function TEXT)")
    c.execute(f'''INSERT INTO AI(name, super_keywords, keywords, antikeywords, script_function) VALUES(?, ?, ?, ?, ?)''', ai_entry)

    # Commit changes
    done()
  elif option == 'edit':
    c.execute('SELECT name FROM AI')
    rows = c.fetchall()
    index=0
    for entry in rows:
      print(f'{index}) {entry}')
      index+=1
    option = int(input("Option: "))
    name=rows[option][0]
    columns = ['name', 'super_keywords', 'keywords', 'antikeywords', 'script_function']
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
  elif option == 'unteach':
    print('Deleting AI entry')
    c.execute(f'SELECT name FROM AI')
    actions = c.fetchall()
    index=0
    for action in actions:
      print(f'{index}) {action}')
      index+=1
    option = int(input('Option: '))
    name=actions[option][0]
    c.execute(f'DELETE FROM AI WHERE name = "{name}"')
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