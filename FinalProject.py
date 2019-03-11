# Eli Mason
# Final Project
# Soccer Shot Percentage

total = 0

name = input('What is your name?: ')
how_many_games = int(input( '\n' 'How many games would you like to Average?: '))

for i in range(how_many_games):
    num_shots = int(input( '\n' 'How many shots did you take this game?: '))
    total = total + num_shots

average = total / how_many_games

print('Shot Percentage: ' + str(round(average, 2)))