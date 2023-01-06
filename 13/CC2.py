#Name
#Period

#leave this code or testing won't work
import random, sys
if len(sys.argv)-1:
	try:
		random.seed(int(sys.argv[1]))
	except:
		pass
#########################################################

#I don't know wher to put this
class Critter():
	"""A virtual pet"""
	def __init__(self, name):
		self.name = name
		self.hunger = random.randint(0, 10)
		self.boredom = random.randint(0, 10)

	def __pass_time(self):
		self.hunger += 1
		self.boredom += 1
	@property
	def mood(self):
		unhappiness = self.hunger + self.boredom
		if unhappiness < 5:
			m = "happy"
		elif 5 <= unhappiness <= 10:
			m = "okay"
		elif 11 <= unhappiness <= 15:
			m = "frustrated"
		else:
			m = "mad"
		return m

	def talk(self):
		rep = f"I'm {self.name} and I feel {self.mood} now."
		crit = Critter(self.name)
		self.__pass_time()
		return rep

	def eat(self, food):
		rep = "Brruppp. Thank you."
		self.hunger -= food
		if self.hunger < 0:
			self.hunger = 0
		self.__pass_time()
		return rep

	def play(self, fun):
		rep = "Wheee!"
		self.boredom -= fun
		if self.boredom < 0:
			self.boredom = 0
		self.__pass_time()
		return rep

	def __str__(self):
		thing = f"Critter Object\nName: {self.name}\nHunger: {self.hunger}\nBoredom: {self.boredom}\nMood: {self.mood}"
		return thing

def main():
	crit_name = input("What do you want to name your critter?\n")
	crit = Critter(crit_name)

	choice = None
	while choice != "0":
		print \
		("""
Critter Caretaker

0 - Quit
1 - Listen to your critter
2 - Feed your critter
3 - Play with your critter""")

		choice = input("Choice:\n")

		# exit
		if choice == "0":
			print("Goodbye.")

		# listen to your critter
		elif choice == "1":
			print(crit.talk())

		# feed your critter
		elif choice == "2":
			feed = int(input('How much food do you want to feed your critter?\n'))
			print(crit.eat(feed))

		# play with your critter
		elif choice == "3":
			fun = int(input('How much fun do you and your critter have?\n'))
			print(crit.play(fun))

		#secret backdoor
		elif choice == "14":
			print(crit)

		# some unknown choice
		else:
			print(f"Sorry, but {choice} isn't a valid choice.")
if __name__ == '__main__':
	main()
