import os
import shutil

# ! Work in progress
# params: src, destination
def move_folder():
  # Home folder
  print("MOVED FOLDER WOOO HOOO")
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
