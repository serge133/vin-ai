import os
import shutil
import printing
from name_inference import name_inference_engine

working_folder = '/Users/michaelbatrakov/Desktop/Python/AOSA/test'

# The engine always provides the lowercase sentence
# This is where the name inference engine is used

def goodbye():
  printing.ai_speak('Have a nice day :)')
  # print('good bye')

# ? Each of these actions have one parameter called sentence
# ? sentence is what the user said to trigger this function
# ? It is helpful if you want to extract data from the sentence

def create_folder(sentence):
  # folder_name = str(input("Name of the Folder: "))
  # folder_location = str(input('Where should this folder be? '))
  name_inference_prewords = ['named', 'called']
  # Gets next element after the preword if exists
  
  name_inference = name_inference_engine(name_inference_prewords, sentence)
  
  printing.print_action('CREATING FOLDER')
  curr_working_directory = os.getcwd()
  # If folder_to_create could not parse user's speech then a folder with a unique id is created
  folder_locations = ['desktop', 'documents', 'python', 'react native', 'react']
  
  print(' - FOLDER LOCATIONS - ',
    *folder_locations,
    sep='\n'
  )
  # folder_location = ai_ask(f'Where to create the folder', '')
  printing.ai_speak("Where to create the folder?")
  folder_location = str(printing.user_input())
  
  if folder_location in folder_locations:
    printing.print_action(f'CREATING A FOLDER IN "{folder_location}"')
    printing.ai_speak("What is the name of the folder")
    folder_to_create = ''
    if name_inference:
      folder_to_create = name_inference
    else:
      folder_to_create = str(printing.user_input())

    try:
      os.mkdir(f'{working_folder}/{folder_to_create}')
      printing.print_action(f"CREATED {folder_to_create}")
      goodbye()
    except:
      printing.print_error(f'Could not make folder "{folder_to_create}" :(')
    
  else:
    printing.print_error('Incorrect Folder')
# ------------------------------------------------------------------------------------
def delete_folder(sentence):
  trash_folder = '.trash'
  printing.print_action(f"MOVING FOLDERS FROM {working_folder} TO TRASH")
  files = os.listdir(working_folder)
  print(
    '- FOLDERS -',
    *files,
    sep='\n'
  )
  printing.ai_speak('What folder do you want to delete?')

  name_inference_prewords = ['called', 'named']
  name_inference = name_inference_engine(name_inference_prewords, sentence)
  folder_to_delete = ''
  if name_inference:
    folder_to_delete = name_inference
  else:
    folder_to_delete = str(printing.user_input())
  # if not folder_to_delete:
  #   print_error('Folder not specified')

  try:
    # shutil.rmtree(f'{working_folder}/{folder_to_delete}')
    shutil.move(f'{working_folder}/{folder_to_delete}', f'{working_folder}/{trash_folder}')
    printing.print_action(f"DELETED {folder_to_delete}")
    goodbye()
  except:
    printing.print_error(f'Could not delete {folder_to_delete} :(')

    

# ! Work in progress
# params: src, destination
def move_folder():
  # Home folder
  print("MOVED FOLDER WOOO HOOO", name)
  # home_folder='/Users/michaelbatrakov'
  # name_array=str(src).split('/')
  # name_of_folder=name_array[len(name_array)-1]
  # print('activating move folder')
  # print(f'{home_folder}/{src}', f'{home_folder}/{destination}/{name_of_folder}', sep='\n')
  # # shutil.move(f'{home_folder}/{src}', f'{home_folder}/{destination}/name-of-file')

def rename_folder():
  folder_to_rename=ai_ask('What folder do you want me to rename?', "didn't work")
  print(f'{home_folder}/{src}', f'{home_folder}/{src}', sep='\n')
  # shutil.move(f'{home_folder}/{src}', f'{home_folder}/{src}')

def make_a_note():
  # os.write()
  print("Writing a note is still under construction")
