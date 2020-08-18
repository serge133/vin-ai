import sqlite3
import util
import AIactions

conn = sqlite3.connect('vin.db')
c = conn.cursor()


def new_engine(ask):
  print("TESTING")
  ask_array = ask.split(' ')
  print(ask_array)
  c.execute('SELECT name, super_keywords, keywords, script_function from AI')
  rows = c.fetchall()
  points_array = []
  for row in rows:
    points = 0
    print(f"MEASURING {row[0]}")
    super_keywords=row[1].split(',')
    keywords=row[2].split(',')
    for super_keyword in super_keywords:
      if super_keyword in ask:
        points+=2
        print("-- ",super_keyword, ' matched!')
    for keyword in keywords:
      if keyword in ask:
        points+=1
        print('- ', keyword, ' matched!')
    points_array.append(points)
  largest_index = util.index_of_largest_element(points_array)
  print(rows[largest_index], 'won')
  script = rows[largest_index][3]
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
    keywords=str(input("[keywords] ({name} are named variables) (sep=,): " )).strip()
    anti_keywords=str(input("[ANTI keywords]These keywords will abort the execution process (sep=,): ")).strip()
    script_function=str(input("Make sure to check with your scripts in ai-actions.py (e.g. move_folder): ")).strip()
  # Creates Table
    ai_entry=(name, super_keywords, keywords, anti_keywords, script_function)
    c.execute("CREATE TABLE IF NOT EXISTS AI(name TEXT, super_keywords TEXT, keywords TEXT, antikeywords TEXT, script_function TEXT)")
    c.execute('''INSERT INTO AI(name, super_keywords, keywords, antikeywords, script_function) VALUES(?, ?, ?, ?, ?)''', ai_entry)

    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    done()
  elif option == 'reteach':
    print('Editing AI')
    name=str(input("Name: "))
    edit_what = str(input('Edit which category [name, super_keywords, keywords, antikeywords, script_function]: '))
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