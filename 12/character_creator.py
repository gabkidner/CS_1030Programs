#Gabe
#4th

MENU = '''
\t\t\t ____
\t\t\t|Menu|
\t\t0 - Quit
\t\t1 - View Attributes and Pool
\t\t2 - Add to Attribute
\t\t3 - Remove from Attribute'''

atts = {"Strength": 0,
		"Dexterity": 0,
		"Constitution": 0,
		"Wisdom": 0,
		"Intelligence": 0,
		"Charisma": 0,
		"Pool": 72}
def table(atts):
	return f'''
______________________________
Strength    |\t{atts['Strength']}
Dexterity   |\t{atts['Dexterity']}
Constitution|\t{atts['Constitution']}
Wisdom      |\t{atts['Wisdom']}
Intelligence|\t{atts['Intelligence']}
Charisma    |\t{atts['Charisma']}
Pool        |\t{atts['Pool']}
______________________________'''

def add(attribute, amount, atts):
	if attribute in atts:
		if amount <= atts['Pool']:
			atts['Pool'] -= amount
			atts[attribute]+=amount
			return f'''{amount} added to {attribute}'''
		else:
			return f'''{amount} is more points than you have left in your pool'''
	else:
		return (f"""'{attribute}' is not a valid attribute""")

def remove(attribute, amount, atts):
	if attribute in atts:
		if amount <= atts[attribute]:
			atts[attribute] -= amount
			atts['Pool'] += amount
			return f'''{amount} removed from {attribute}'''
		else:
			return f'''{amount} is more points than you have left in {attribute}'''
	else:
		return f"""'{attribute}' is not a valid attribute"""

def main():
	play = True
	while play:
		print(MENU)
		choice = input("What's your choice?\n")
		while choice not in ('0','1','2','3'):
			print(f"'{choice}' is not a valid menu option.")
			print(MENU)
			choice = input("What's your choice?\n")
		if choice == '0':
			play = False
		elif choice == '1':
			print(table(atts))
		elif choice == '2':
			attribute = input('What attribute would you like to add points to?\n').capitalize()
			amount = int(input(f'How many points would you like to add?\n'))
			print(add(attribute, amount, atts))
		else:
			attribute = input('What attribute would you like to remove points from?\n').capitalize()
			amount = int(input(f'How many points would you like to remove?\n'))
			print(remove(attribute, amount, atts))
	print('Goodbye.')

#keep this at the bottom of your program
if __name__ == "__main__":
	main()
