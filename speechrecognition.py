import speech_recognition as sr

def ai_ask(message, fallback):
  print(message)
  # The user's answer
  response = ""
  r = sr.Recognizer()                 # initialize recognizer
  with sr.Microphone() as source:     # mention source it will be either Microphone or audio files.
      audio = r.listen(source)        # listen to the source
      try:
          response = r.recognize_google(audio)    # use recognizer to convert our audio into text part.
          print(response)
      except:
          print("Something didn't work, using fallback")  
          response = fallback
  return response