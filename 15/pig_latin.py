#Name
#Period
VOWELS = 'aeiou'
END = '.,!?'

def read(file):
	try:
		text_file = open(file)
		lines = text_file.readlines()
		text_file.close()
	except IOError:
		return ['1error']
	return lines
def write(message):
	text_file = open("pig.txt", "w")
	text_file.writelines(message)
	text_file.close()
	return message

def way_end(word):
	for x in word:
		if x in END:
			ind = word.index(x)
			inde = word[ind]
			word = word[0:ind]
			return f'{word}way{inde}'
	return f'{word}way'

def ay_end(word,index):
	x = word[0:index]
	word = word[index:]
	for a in word:
		if a in END:
			ind = word.index(a)
			inde = word[ind]
			word = word[0:ind]
			return f'{word}{x}ay{inde}'
	return f'{word}{x}ay'

def translate(message):
	pig = []
	for line in message:
		line = line.strip().lower()
		words = line.split(" ")
		new = []
		for word in words:
			if word[0] in VOWELS:
				new.append(way_end(word))
			elif word[0].isalpha():
				for letter in word:
					if letter in VOWELS:
						index = word.index(letter)
						break
				new.append(ay_end(word,index))
			else:
				new.append(word)
		pig.append(" ".join(new) + '\n')
	return pig


def main():
	print("Welcome to the Pig Latin Translator!")
	file = input("What is the name of the file:\n")
	message = read(file)
	new = translate(message)
	write(message)
	print("Message stored in 'pig.txt'")

if __name__ == "__main__":
	main()
