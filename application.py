import tkinter as tk
import getpass
import engine
# // import printing

window = tk.Tk()
window.title('AOSA')
Label = tk.Label(window, text="Artificially Optimized System Assistant")
Label.grid(row=1, column=2)

ai = tk.StringVar(window)
user = tk.StringVar(window)

ai.set(f"AI - I'm AOSA. You are {getpass.getuser()}")

AILabel = tk.Label(window, textvariable=ai, fg='blue')
AILabel.grid(row = 2, column=2)

UserLabel = tk.Label(window, textvariable=user, fg='red')
UserLabel.grid(row=3, column=2)

action = tk.StringVar()

ActionLabel = tk.Label(window, textvariable=action, fg='green')
ActionLabel.grid(row=4,column=2)

Input = tk.Entry(window)
Input.grid(row=5,column=2)



def ai_speak(message):
  ai.set(f'AI - {message}')

def execute():
  input_text = Input.get()
  # printing.user.set(f'YOU - {input_text}')
  engine.ai(input_text)


Button = tk.Button(window, text="Execute", command=execute)


Button.grid(row = 5, column=3)
window.mainloop()
