#Gabe
#4th

#leave this code or testing won't work
import random, sys
if len(sys.argv)-1:
	random.seed(int(sys.argv[1]))
#########################################################
#Variables
H=0
T=0
x=0
Flips=input("How many times do you want to flip the coin?\n")
print(f"The coin was flipped {Flips} times.")
F=int(Flips)
while x != F:
	x += 1
	R=random.randrange(2)
	if R == 0:
		T += 1
	else:
		H += 1
print(f'Heads: {H}\tTails: {T}')
