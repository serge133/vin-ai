import os
import getpass
import shutil
import printing
from name_inference import name_inference_engine

user = getpass.getuser()
working_folder = f'/Users/{user}'

# The engine always provides the lowercase sentence
# This is where the name inference engine is used

def goodbye():
  printing.ai_speak('Have a nice day :)')
  # print('good bye')

# ? Each of these actions have one parameter called sentence
# ? sentence is what the user said to trigger this function
# ? It is helpful if you want to extract data from the sentence
folder_locations = [
  f'{working_folder}/Desktop', 
  f'{working_folder}/Documents', 
  f'{working_folder}/Desktop/Python', 
  f'{working_folder}/Desktop/React Native/', 
  f'{working_folder}/Desktop/React', 
  f'{working_folder}/Desktop/Python/Aosa/test'
]

def create_folder(sentence):
  printing.print_action('CREATING FOLDER')
  # folder_name = str(input("Name of the Folder: "))
  # folder_location = str(input('Where should this folder be? '))
  # Gets next element after the preword if exists
  
  name_inference_prewords = ['named', 'called']
  name_inference = name_inference_engine(name_inference_prewords, sentence)
  
  curr_working_directory = os.getcwd()
  # If folder_to_create could not parse user's speech then a folder with a unique id is created
  index=0
  for folder in folder_locations:
    print(f'{index}) {folder}')
    index+=1
  # print(' - FOLDER LOCATIONS - ',
  #   *folder_locations,
  #   sep='\n'
  # )
  # folder_location = ai_ask(f'Where to create the folder', '')
  printing.ai_speak("Where to create the folder?")
  option = int(printing.user_input())
  folder_location = folder_locations[option]
  
  if folder_location in folder_locations:
    printing.print_action(f'CREATING A FOLDER IN "{folder_location}"')
    folder_to_create = ''
    if name_inference:
      folder_to_create = name_inference
    else:
      printing.ai_speak("What is the name of the folder")
      folder_to_create = str(printing.user_input())

    try:
      os.mkdir(f'{folder_location}/{folder_to_create}')
      printing.print_action(f"CREATED {folder_to_create} FOLDER")
      goodbye()
    except:
      printing.print_error(f'Could not make folder "{folder_to_create}" :(')
    
  else:
    printing.print_error('Incorrect Folder')
# ------------------------------------------------------------------------------------
def delete_folder(sentence):
  printing.print_action("MOVING FOLDERS TO TRASH")

  trash_folder = f'/Users/{user}/.aosa_trash'
  name_inference_prewords = ['called', 'named']
  name_inference = name_inference_engine(name_inference_prewords, sentence)


  printing.ai_speak("Where to delete a folder?")
  
  index=0
  for folder in folder_locations:
    print(f'{index}) {folder}')
    index+=1

  option = int(printing.user_input())
  folder_location = folder_locations[option]

  if folder_location in folder_locations:
    printing.print_action(f'DELETING FOLDER IN {folder_location}')

    files = os.listdir(folder_location)
    print(
      '- FOLDERS -',
      *files,
      sep='\n'
    )
    printing.ai_speak('What folder do you want to delete?')

    folder_to_delete = ''
    if name_inference:
      folder_to_delete = name_inference
    else:
      folder_to_delete = str(printing.user_input())
    # if not folder_to_delete:
    #   print_error('Folder not specified')

    try:
      # shutil.rmtree(f'{home_folder}/{folder_to_delete}')
      shutil.move(f'{folder_location}/{folder_to_delete}', trash_folder)
      printing.print_action(f"DELETED {folder_to_delete}")
      goodbye()
    except:
      printing.print_error(f'Could not delete {folder_to_delete} :(')
  else:
    printing.print_error("Folder doesn't exist :(")

    

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
  print(f'{working_folder}/{src}', f'{working_folder}/{src}', sep='\n')
  # shutil.move(f'{home_folder}/{src}', f'{home_folder}/{src}')

def make_a_note():
  # os.write()
  print("Writing a note is still under construction")
