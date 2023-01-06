#Name
#Period
class Remote():
	def __init__(self):
		self.__channel = 3
		self.__volume = 5

	def __str__(self):
		return f"Channel: {self.__channel}\nVolume: {self.__volume}"

	def volume_up(self):
		self.__volume += 1
		if self.__volume <= 10:
			return self.__volume
		else:
			self.__volume = 10
			return self.__volume

	def volume_down(self):
		self.__volume -= 1
		if self.__volume >= 0:
			return self.__volume
		else:
			self.__volume = 0
			return self.__volume

	def channel_up(self):
		self.__channel += 1
		if self.__channel <= 100:
			return self.__channel
		else:
			self.__channel = 1
			return self.__channel

	def channel_down(self):
		self.__channel -= 1
		if self.__channel >= 1:
			return self.__channel
		else:
			self.__channel = 100
			return self.__channel

	def set_channel(self, new_channel):
		try:
			inte = int(new_channel)
			if inte > 100 or inte < 1:
				print(f"'{new_channel}' is out of the channel range")
			else:
				self.__channel = inte

		except ValueError as blah:
			print(f"Error: {blah}\nExplanation: '{new_channel}' isn't a number")

	@property
	def channel(self):
		return self.__channel
	@channel.setter
	def channel(self, new_channel):
		try:
			tri = int(new_channel)
		except ValueError as blah:
			print(f"Error: {blah}\nExplanation: '{new_channel}' isn't a number")
		if new_channel > 100 or new_channel < 1:
			print(f"'{new_channel}' is out of the channel range")

def main():
	r = Remote()
	print(r)
	user = ''
	MENU = '''
vu - Volume Up
vd - Volume Down
cu - Channel Up
cd - Channel Down
set - Set Channel
q - Quit
'''
	while user != 'q':
		print(MENU)
		user = input("Select an option:\n")
		if user == 'vu':
			r.volume_up()
		elif user == 'vd':
			r.volume_down()
		elif user == 'cu':
			r.channel_up()
		elif user == 'cd':
			r.channel_down()
		elif user == 'set':
			r.set_channel(input("What channel?\n"))
		elif user == 'v':
			print(r)
		elif user == 'q':
			print("Goodbye.")
		else:
			print(f"{user} is not a valid option")

if __name__ == '__main__':
	main()
