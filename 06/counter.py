#Gabe Kidner
#4th

S=int(input('What is the starting number?\n'))
E=int(input('What is the ending number?\n'))
C=int(input('How much should I count by?\n'))
print(f'Counting from {S} to {E} by {C}:')
if C < 0:
	E -= 1
else:
	E += 1
Result = ""
for x in range(S, E, C):
	Result += f"{x} "
print(Result)
