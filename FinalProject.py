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


try:
    how_many_games = int(input('How many games would you like to average?: '))
    print('Is this the amount of games you would like to average? (If not please refresh): ', str(how_many_games))
except ValueError:
    print('That was not an integer')


#The for loop will
for i in range(how_many_games):
    num_shots = int(input( '\n' 'How many shots did you take this game?: '))
    num_shots_made = int(input('How many shots did you make this game?: '))
    total = total + num_shots
    totals = totals + num_shots_made


x = average
while x > -1:
    print(x)
    break

average = total / totals
#This will print the final average of your goals.
>>>>>>> Try_and_Except
print('Shot Percentage: ' + str(round(average, 2)))