#Name
#Period

# Word Jumble
#
# The computer picks a random word and then "jumbles" it
# The player has to guess the original word

#leave this code or testing won't work
import random, sys
if len(sys.argv)-1:
	random.seed(int(sys.argv[1]))
#########################################################
bruh = ''
# create a sequence of words to choose from
WORDS = ("python", "jumble", "easy", "difficult", "answer")
# pick one word randomly from the sequence
word = random.choice(WORDS)
# create a variable to use later to see if the guess is correct
correct = word

# create a jumbled version of the word
jumble =""
while word:
	position = random.randrange(len(word))
	jumble += word[position]
	word = word[:position] + word[(position + 1):]
hinted = 0
guess = 'guess'
# start the game
print("\t\tWelcome to Word Jumble!\n\n\tUnscramble the letters to make a word.\n(Press the enter key at the prompt to quit.)\n")
print(f"The jumble is: {jumble}\n")
while guess != correct and guess != "":
	guess = input("Your guess:\n")
	if guess == correct and hinted == 0:
		print("That's it! You guessed it!\nGood job not using a hint!")
		print("Thanks for playing.")
	elif guess == correct and hinted >= 1:
		print("That's it! You guessed it!\nTry to not use a hint next time.")
		print("Thanks for playing.")
	elif guess == bruh:
		print('Goodbye.')
	elif guess == '?' and correct == 'answer':
		print("what you're looking for")
		hinted += 1
	elif guess == '?' and correct == 'difficult':
		print('not easy')
		hinted += 1
	elif guess == '?' and correct == 'easy':
		print('not hard')
		hinted += 1
	elif guess == '?' and correct == 'jumble':
		print('the name of the game')
		hinted += 1
	elif guess == '?' and correct == 'python':
		print('a slithery coding language')
		hinted += 1
	elif guess != correct and hinted == 0:
		print("Sorry, that's not it.\nType '?' if you want a hint.")
	elif guess != correct and hinted != 0:
		print("Sorry, that's not it.")
