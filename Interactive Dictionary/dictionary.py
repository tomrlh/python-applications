import json
from difflib import get_close_matches

data = json.load(open("data.json", "r"))
keep_running = "y"

def get_word_definition(word):
	try:
		word = word.lower()
		if word in data:
			for definition in data[word]:
				print(" - " + definition)
		elif(len(get_close_matches(word, data.keys()))) > 0:
			return "Did you mean '%s' instead?" % get_close_matches(word, data.keys())[0]
	except KeyError:
		return "The word '" + word + "' doesn't exist in the dictionary"



while(keep_running == "y"):
	word = input("Insert a word: ")
	print("\n")
	print(get_word_definition(word))

	keep_running = input("\nWant to keep searching? y/n\n")

