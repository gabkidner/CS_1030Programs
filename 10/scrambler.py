#NameMessage
#Period

#leave this code or testing won't work
import random, sys
if len(sys.argv)-1:
	random.seed(int(sys.argv[1]))
#########################################################

#start message
Original = input('What is the message to scramble?\n')
#not printed
Original_List = Original.split(' ')
random.shuffle(Original_List)
Shuffled = " ".join(Original_List)
#number of words and end message
print(f'There are {len(Original_List)} words in the message.')
print(f"Here's the shuffled message:\n{Shuffled}")
