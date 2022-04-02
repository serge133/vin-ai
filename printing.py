AI = '\033[94m'
USER = '\033[95m'
BOLD = '\033[1m'
FAIL = '\033[91m'
WARNING = '\033[93m'
UNDERLINE = '\033[4m'
ENDC = '\033[0m'
OKGREEN = '\033[92m'


def ai_speak(message, pre=""):
    print(f'{pre}{AI}Alexis - {message}{ENDC}')


def user_input():
    return input(f'{USER}YOU - {ENDC}')


def print_action(message):
    print(f'{BOLD}ACTION - {message}{ENDC}')


def print_error(message):
    print(f'{FAIL}ERROR - {message}{ENDC}')


def print_good(message, bold=False):
    print(f'\t{BOLD if bold else ""}{OKGREEN}{message}{ENDC}')


def print_eh(message):
    print(f'\t{WARNING}{message}{ENDC}')


def print_bad(message, bold=False):
    print(f'\t{BOLD if bold else ""}{FAIL}{message}{ENDC}')
