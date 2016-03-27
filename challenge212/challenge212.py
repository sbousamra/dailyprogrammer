consonants=["B", "C", "D", "F", "G", "H", "J", "K",
"L", "M", "N", "P", "Q", "R", "S",
"T", "V", "W", "X", "Y", "Z"]

def isConsonant(letter):
	if letter.upper() in consonants:
		return True
	else: 
	 	return False

fname = "input212.txt"
with open(fname) as file:
	bass=file.read().splitlines()
	for line in bass:
		alteredline=""
		for character in line:
			if isConsonant(character):
				alteredline = alteredline + (character + "o" + character.lower())
			else:
				alteredline = alteredline + character
 
		print(alteredline)