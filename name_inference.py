import printing

def name_inference_engine(prewords, lowercase_sentence):
  sentence_array = lowercase_sentence.split(' ')
  for preword in prewords:
    if preword in lowercase_sentence:
      preword_index = sentence_array.index(preword)
      if preword_index + 1 < len(sentence_array):
        name_inference = sentence_array[preword_index + 1]
        printing.print_action(f"NAME INFERENCED -> {name_inference}")
        return name_inference
      else: 
        return False
