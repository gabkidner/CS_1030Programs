#Name
#Period

#leave this code or testing won't work
import random, sys
if len(sys.argv)-1:
	random.seed(int(sys.argv[1]))
#########################################################
#establishes the dice number and sides
Total = 0
Dice = int(input('How many dice would you like to roll?\n'))
Sides = int(input('How many sides do the dice have?\n'))
print(f"Rolling {Dice}x d{Sides}.")
Rolls = 0
#rolls the dice
while Rolls != Dice:
	Rolls += 1
	x=random.randint(1,Sides)
	print(f'Roll {Rolls}: {x}')
	Total += x
print(f'Total: {Total}')
