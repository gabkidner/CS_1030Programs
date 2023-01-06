#Gabe
#4th
#leave this code or testing won't work
import random, sys
if len(sys.argv)-1:
	random.seed(int(sys.argv[1]))
#########################################################

print("\tWelcome to 'Guess My Number 2.0'!")
print("\nI'm thinking of a number between 1 and 100.")
print("You have 6 attempts to guess my number.")

# set the initial values
the_number = random.randint(1, 100)
tries = 1
guess = 2

# guessing loop
while guess != the_number and tries <= 6:
	guess = int(input(f"Take guess number {tries}:\n"))
	if guess != the_number and tries == 6:
		print(f"You ran out of tries! The number was {the_number}.")
	elif guess < the_number:
		print("Higher...")
	elif guess > the_number:
		print("Lower...")
	else:
		print(f'You guessed it! The number was {the_number}.')
		print(f'And it only took you {tries} tries!')
	tries += 1
