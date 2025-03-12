def greet(name):
	if l == 'english':
		print("Hello, " + str(name))
	elif l == 'spanish':
		print("Hola, " + str(name))
	elif l == 'german':
		print("Hallo, " + str(name))


def lang_selection():
	lang = input("Pick your language: german, spanish, english ")
	return lang

def english(lang):
	return  "What is your name?  "

def spanish(lang):
	return "¿cómo te llamas? "

def german(lang):
	return "wie heißt du? "

def name_input(x):
	if x == 'german':
		name = input("wie heißt du? ")
		return name
	elif x == 'spanish':
		name = input('¿cómo te llamas? ')
		return name
	elif x == 'english':
		name = input('What is your name? ')
		return name


l = lang_selection()
x = name_input(l)
greet(x)












