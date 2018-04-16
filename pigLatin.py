def info_text():
  print("Options:\n(1) Convert to Pig Latin\n(2) Convert to Latin\n")

def input_checker():
  proper = False
  while (proper != True):
    user_in = (input("Option:"))
    if (user_in not in ('1','2')):
      print("Please type 1 or 2.")
    else:
      proper = True
  return int(user_in)
  
def end_adder():
  ender = input("Modification text: ")
  return ender

def doer():
  user_in = input_checker()
  word_input = ''
  if(user_in == 1):
    word_input = input("Latin:").lower()
  elif(user_in == 2):
    word_input == input("Pig Latin:").lower()
  
  text_input = word_input.split()
  printer(converter(text_input, user_in), user_in)
  
def converter(text_input, user_in):
  output = []
  for word in text_input:
    if(user_in == 1):
      output.append(pig_latin(word))
    elif(user_in == 2):
      output.append(latin(word))
  return output

def printer(output, user_in):
  if(user_in == 1):
    print("Pig latin: ", end='')
    for words in output:
      print(words, end=' ')
  elif(user_in == 2):
    print("Latin: ", end='')
    for words in output:
      print(words, end=' ')

def pig_latin(word):
  first_letter = word[0]
  end_chars = end_adder()  
  if (first_letter in 'aeiou'):
    pig_word = word + end_chars
  else:
    pig_word = word[1:]+word[0]+end_chars
  
  return pig_word

def latin(word):
  word = word[0:len(word)-2]
  latin_word = word
  if (latin_word[-1] in 'aeiou'):
    return latin_word
  else:
    latin_word = word[-1]+word[0:len(word)-1]
    return latin_word

info_text()
doer()
