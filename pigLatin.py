def info_text():
	print("Options:\nType 'pig latin' to convert to Pig Latin\nType 'latin' to convert to Latin\n")

def input_checker():
	proper = False
	while (proper != True):
		user_in = (input("Option:"))
		if (user_in.lower() not in ('latin', 'pig latin')):
			print("Please type 'latin' or 'pig latin'.")
		else:
			proper = True
	return user_in

def end_adder():
  passed = False
  while (passed != True):
    ender = input("Mod text:")
    if(ender.isalpha()):
      passed = True
    else:
      print("Please use only alphabets.")
  return ender

def pig_latin_word(word, end_chars):
	first_letter = word[0]
	if (word[-1] in '.',',',';',':','!','?'):
	  end_chars += word[-1]
	  word = word[:-1]
	if (first_letter in 'aeiou'):
		pig_word = word + end_chars
	else:
		pig_word = word[1:] + word[0] + end_chars

	return pig_word

def latin_word(word, end_chars):
  if (word[-1] in '.',',',';',':','!','?'):
    end_chars += word[-1]
    word = word[0:len(word) - len(end_chars)]
  else:
	  word = word[0:len(word) - len(end_chars)]
  latinWord = word
  if (latinWord[-1] in 'aeiou'):
    return latinWord
  elif (len(latinWord)<=2 and latinWord[0] in 'aeiou'):
    return latinWord
  else:
    latinWord = word[-1] + word[0:len(word)-1]
    return latinWord

def converter(text_input, user_in, end_chars):
  output=[]
  for word in text_input:
    if user_in == "pig latin":
      output.append(pig_latin_word(word,end_chars))
    if user_in == "latin":
      output.append(latin_word(word,end_chars))
  return output

def printer(output, user_in):
	if (user_in == 'pig latin'):
		print("Pig latin:", end=' ')
		for words in output:
			print(words, end=' ')
	elif (user_in == 'latin'):
		print("Latin:", end=' ')
		for words in output:
			print(words, end=' ')

def do():
	user_in = input_checker()
	word_input = ''
	if (user_in == 'pig latin'):
		word_input = input("Latin:").lower()
	elif (user_in == 'latin'):
		word_input = input("Pig Latin:").lower()
	else:
	  word_input = input("Debug input:").lower() 
	
	text_input = word_input.split()
	printer(converter(text_input, user_in, end_adder()), user_in)


info_text()
do()
