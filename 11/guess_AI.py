#Gabe
#4th

#leave this code or testing won't work
import random, sys
if len(sys.argv)-1:
	try:
		random.seed(int(sys.argv[1]))
	except:
		pass
#########################################################

def end(tries, user):
	if user == 'correct' and tries <= 6:
		user = f"I knew I could beat you, and in {tries} tries too!\nGoodbye."
		return user
	else:
		user = "I ran out of tries! You bested me!\nGoodbye."
		return user
	return user
def high_low(low, high, guess, user, tries, play):
	if tries == 6 or user == 'correct':
		play = False
	elif user == 'high':
		high = guess-1
		tries += 1
	elif user == 'low':
		low = guess + 1
		tries += 1
	return low, high, tries, play
def ask():
	user = input("Am I 'high', 'low', or 'correct'?\n").lower()
	while user not in ("high", "low", "correct"):
		user = input("Am I 'high', 'low', or 'correct'?\n").lower()
	return user
def main():
	print("I am a special mind-reading machine and will guess the number you're thinking of between 1 and 100 in 6 tries or less.")
	print("After each guess, tell me if I'm 'high', 'low', or 'correct'.")

	high = 100
	low = 1
	play = True
	tries = 1
	while play:
		guess = random.randint(low, high)
		print(f"For try {tries} I guess {guess}")
		user = ask()
		low, high, tries, play = high_low(low, high, guess, user, tries, play)
	print(end(tries, user))

if __name__ == "__main__":
	main()
