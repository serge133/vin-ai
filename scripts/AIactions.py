import printing
# import executable
# from engine import verbose_ai

def calculator(sentence):
  printing.print_action("CALCULATOR (leave)")
  # printing.ai_speak("You can: +/*-**")
  expression = printing.user_input()
  if expression == 'leave':
    return
  print(eval(expression))
  calculator("")
