import os
import shutil
from speechrecognition import ai_ask
import uuid
from coloring_terminal import bcolors

working_folder = '/Users/michaelbatrakov/Desktop/Python/walner/test'

def goodbye():
  print('Have a nice day :)')

# ! None of these should have parameters

def print_action(message):
  print(f'{bcolors.BOLD}ACTION - {message}{bcolors.ENDC}')
def print_error(message):
  print(f'{bcolors.FAIL}ERROR - {message}{bcolors.ENDC}')

def create_folder():
  # folder_name = str(input("Name of the Folder: "))
  # folder_location = str(input('Where should this folder be? '))
  print_action('CREATING FOLDER')
  curr_working_directory = os.getcwd()
  # If folder_to_create could not parse user's speech then a folder with a unique id is created
  folder_locations = ['desktop', 'documents', 'python', 'react native', 'react']
  
  print(' - FOLDER LOCATIONS - ',
    *folder_locations,
    sep='\n'
  )
  folder_location = ai_ask(f'Where to create the folder', '')
  
  if folder_location in folder_locations:
    print_action(f'CREATING A FOLDER IN "{folder_location}"')
    folder_to_create = ai_ask("What is the name of the folder?", str(uuid.uuid1()))
    confirm = ai_ask(f'Is folder name "{folder_to_create}" correct? [yes, no]', 'no')
    if confirm == 'yes':
      try:
        os.mkdir(f'{working_folder}/{folder_to_create}')
        goodbye()
      except:
        print_error(f'Could not make folder "{folder_to_create}" :(')
    else:
      print_error('No Confirmation')
  else:
    print_error('Incorrect Folder')

def delete_folder():
  print_action(f"DELETING FOLDER IN {working_folder}")
  files = os.listdir(working_folder)
  print(*files, sep='\n')
  folder_to_delete = ai_ask("What folder should I delete?", False)

  if not folder_to_delete:
    print_error('Folder not specified')

  confirm = ai_ask(f'I am going to delete {folder_to_delete}, are you sure [yes, no]', 'no')
  if confirm == 'yes':
    try:
      shutil.rmtree(f'{working_folder}/{folder_to_delete}')
      goodbye()
    except:
      print_error(f'Could not delete {folder_to_delete} :(')
  else:
    print('No Confirmation')

    

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
