import os
import shutil
import speech_recognition as sr     # import the library

home_folder = '/Users/michaelbatrakov/Desktop'


def ai_confirm(message):
  print(message)
  r = sr.Recognizer()                 # initialize recognizer
  with sr.Microphone() as source:     # mention source it will be either Microphone or audio files.
      audio = r.listen(source)        # listen to the source
      try:
          text = r.recognize_google(audio)    # use recognizer to convert our audio into text part.
          print(text)
          if text == 'yes':
            return True
          else:
            return False
      except:
          print("Something didn't work")  
          return False  # In case of voice not recognized  clearly


def create_folder(name):
  print(f"I will create {name} for you sir")
  os.mkdir(f'{home_folder}/{name}')

def delete_folder(name):
  if ai_confirm('Are you sure?'):
    shutil.rmtree(f'{home_folder}/{name}')

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
