AI = '\033[94m'
USER = '\033[95m'
BOLD = '\033[1m'
FAIL = '\033[91m'
WARNING = '\033[93m'
UNDERLINE = '\033[4m'
ENDC = '\033[0m'

def ai_speak(message):
  print(f'{AI}AI - {message}{ENDC}')
  # AILabel = tk.Label(window, text=message)
  # AILabel.grid(row = 2, column=2)


def user_input(): 
  return input(f'{USER}YOU - {ENDC}')

def print_action(message):
  print(f'{BOLD}ACTION - {message}{ENDC}')
def print_error(message):
  print(f'{FAIL}ERROR - {message}{ENDC}')
