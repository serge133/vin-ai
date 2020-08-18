import sqlite3

conn = sqlite3.connect('vin.db')
c = conn.cursor()

def engine(ask):
  ask_array = ask.split(' ')
  c.execute('SELECT name, super_keywords, keywords from AI')
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
  print(points_array)
