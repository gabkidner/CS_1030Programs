#Name
#Period

#leave this code or testing won't work
import random, sys
if len(sys.argv)>1:
	random.seed(int(sys.argv[1]))
#########################################################
print("You crack open your cookie and your fortune falls out:")
x=random.randrange(5)
if x == 0:
	print("Help! I'm being held prisoner in a fortune cookie bakery!")
elif x == 1:
	print('Cookie said: "You really crack me up."')
elif x == 2:
	print('You are not illiterate.')
elif x == 3:
	print('You will read this and say "Geez! I could come up with better fortunes than that!"')
elif x == 4:
	print('This cookie is never gonna give you up, never gonna let you down.')
