import os
import shutil
from speechrecognition import ai_ask

working_folder = '/Users/michaelbatrakov/Desktop/Python/walner/test'


# def ai_confirm(message):
#   print(message)
#   r = sr.Recognizer()                 # initialize recognizer
#   with sr.Microphone() as source:     # mention source it will be either Microphone or audio files.
#       audio = r.listen(source)        # listen to the source
#       try:
#           text = r.recognize_google(audio)    # use recognizer to convert our audio into text part.
#           print(text)
#           if text == 'yes':
#             return True
#           else:
#             return False
#       except:
#           print("Something didn't work")  
#           return False  # In case of voice not recognized  clearly



def create_folder():
  # folder_name = str(input("Name of the Folder: "))
  # folder_location = str(input('Where should this folder be? '))
  curr_working_directory = os.getcwd()
  folder_to_create = ai_ask("What is the name of the folder?", '')
  print('Folder locations')
  folder_location = ''
  print(f"I will create {folder_to_create} at {folder_location} for you sir")
  confirm = ai_ask("Is this correct? [yes, no]", 'no')
  if confirm == 'yes':
    try:
      os.mkdir(f'{working_folder}/{folder_to_create}')
    except:
      print(f'Could not make folder {folder_to_create} :(')
  else:
    print('No Confirmation')

def delete_folder():
  print(f"I am going to delete a folder in {working_folder}")
  files = os.listdir(working_folder)
  print(*files, sep='\n')
  folder_to_delete = ai_ask("What folder should I delete?", '')
  confirm = ai_ask(f'I am going to delete {folder_to_delete}, are you sure [yes, no]', 'no')
  if confirm == 'yes':
    try:
      shutil.rmtree(f'{working_folder}/{folder_to_delete}')
    except:
      print(f'Could not delete {folder_to_delete} :(')
  else:
    print('No Confirmation')

    

# ! Work in progress
# params: src, destination
def move_folder(name):
  # Home folder
  print("MOVED FOLDER WOOO HOOO", name)
  # home_folder='/Users/michaelbatrakov'
  # name_array=str(src).split('/')
  # name_of_folder=name_array[len(name_array)-1]
  # print('activating move folder')
  # print(f'{home_folder}/{src}', f'{home_folder}/{destination}/{name_of_folder}', sep='\n')
  # # shutil.move(f'{home_folder}/{src}', f'{home_folder}/{destination}/name-of-file')

def rename_folder(src, name):
  home_folder='/Users/michaelbatrakov'
  parent_directory=str(src).split('/').pop()
  print('activating rename folder')
  print(f'{home_folder}/{src}', f'{home_folder}/{src}', sep='\n')
  # shutil.move(f'{home_folder}/{src}', f'{home_folder}/{src}')
