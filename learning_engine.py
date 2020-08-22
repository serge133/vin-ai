import sqlite3

conn = sqlite3.connect('vin.db')
c = conn.cursor()

def learning_engine(sentence, best_category, best_match, exclusionary_keywords):
  sentence_array = sentence.split(' ')
  # BEST MATCH INCLUDES
  # best_match[0] = name
  # best_match[1] = super_keywords
  # best_match[2] = keywords
  # best_match[3] = antikeywords
  # best_match[4] = script_function
  print(best_category, best_match, sep='\n')
  # ? First update the catagory
  category_keywords = best_match[2]
  for keyword in sentence_array:
    if keyword not in category_keywords and keyword not in exclusionary_keywords:
      category_keywords+=f',{keyword}'
  c.execute(f'UPDATE AI SET keywords = "{category_keywords}" WHERE name = "{best_category[0]}"')
  # conn.commit()
  # ? Then update in the category
  keywords = best_match[2]
  for keyword in sentence_array:
    if keyword not in keywords and keyword not in exclusionary_keywords:
      keywords+=f',{keyword}'
  c.execute(f'UPDATE {best_category[4]} SET keywords = "{keywords}" WHERE name = "{best_match[0]}"')
  conn.commit()
