#Gabe
#4th

time = 0
reverse = ""
position = 0
message = input('What is your message?\n')
for blank in message:
    reverse = blank + reverse
print('\nYour message reversed is:')
print(f'{reverse}')
