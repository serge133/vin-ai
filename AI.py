from training import train
from ask import ask

print('What do you want to do?', '1) train me?', '2) Ask me?', sep='\n')
option = int(input("Option: "))

if option == 1:
  train()
else:
  ask()