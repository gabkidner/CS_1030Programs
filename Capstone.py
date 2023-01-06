stones = 20;
while stones != 0:
    player = '2'
    input = int(input(f'It is player {player}\'s turn\nHow many stones will you take?\n'))
    while input > 3:
        input = int(input('Invalid input, try again\n'))
    stones -= input
