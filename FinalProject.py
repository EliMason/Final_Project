# Eli Mason
# Final Project
# Soccer Shot Percentage

#This program will tell you your shot to goals percentage.
name = input('What is your name?: ')

#This will ask you for your name.
def greeting():
    print('Hello, ' + name + '!')
    print('')
greeting()

total = 0
totals = 0

#This will ask you how many games you would like the average
how_many_games = int(input( '\n' 'How many games would you like to Average?: '))

#The for loop will
for i in range(how_many_games):
    num_shots = int(input( '\n' 'How many shots did you take this game?: '))
    num_shots_made = int(input('How many shots did you make this game?: '))
    total = total + num_shots
    totals = totals + num_shots_made

average = total / totals

print('Shot Percentage: ' + str(round(average, 2)))