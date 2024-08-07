

user_input1 = input('What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.')


if int(user_input1) == 0:
    print('You have selected "Rock".')
elif int(user_input1) == 1:
    print('You have selected "Paper".')
elif int(user_input1) == 2:
    print('You have selected "Scissors".')
else:
    print('Please select a valid number.')
    user_input1 = input('What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.')