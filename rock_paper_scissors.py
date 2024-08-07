
import random
import math


#logic for selection of rock paper scissors and output of the user selection

#if logic
#user_input1 = input('What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.')
# if int(user_input1) == 0:
#     print('You have selected "Rock".')
# elif int(user_input1) == 1:
#     print('You have selected "Paper".')
# elif int(user_input1) == 2:
#     print('You have selected "Scissors".')
# else:
#     print('Please select a valid number next time.')
#     user_input1 = input('What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.')

#while logic
count  = 0
while count == 0:
    user_input1 = input('What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.')
    if int(user_input1) == 0:
        print('You have selected "Rock".')
        count += 1
    elif int(user_input1) == 1:
        print('You have selected "Paper".')
        count += 1
    elif int(user_input1) == 2:
        print('You have selected "Scissors".')
        count += 1
    else:
        print('Please select a valid number next time.')
    



#randomization of the choice of the computer


computer_choice = random.randint(0,2)

if computer_choice == 0:
    print('The computer has chosen Rock.')
elif computer_choice == 1:
    print('The computer has chosen Paper.')
elif computer_choice == 2:
    print('The computer has chosen Scissors.')
else:
    print('The code be funnny')

#outcome of the match
if computer_choice == 0 and int(user_input1) == 0:
    print('Rock ties with Rock')
elif computer_choice == 0 and int(user_input1) == 1:
    print('Paper beats Rock. /n You Win!!')
elif computer_choice == 0 and int(user_input1) == 2:
    print('Rock beats Scissors. /n You Lose!!')
elif computer_choice == 1 and int(user_input1) == 0:
    print('Paper beats Rock. /n You Lose!!')
elif computer_choice == 1 and int(user_input1) == 1:
    print('Paper ties with Paper')
elif computer_choice == 1 and int(user_input1) == 2:
    print('Scissors beats Paper. /n You Win!!')
elif computer_choice == 2 and int(user_input1) == 0:
    print('Rock beats Scissors. /n You Win!!')
elif computer_choice == 2 and int(user_input1) == 1:
    print('Scissors beats Paper. /n You Lose!!')
elif computer_choice == 2 and int(user_input1) == 2:
    print('Scissors ties with Scissors')
else:
    print('The code be funnny again')


#alternate outcome of the match

# if computer_choice == 0:
#     if int(user_input1) == 0:
#         print('Rock ties with Rock')
#     elif int(user_input1) == 1:
#         print('Paper beats Rock. You Win!!')
#     elif int(user_input1) == 2:
#         print('Rock beats Scissors. You Lose!!')
# elif computer_choice == 1:
#     if int(user_input1) == 0:
#         print('Paper beats Rock. You Lose!!')
#     elif int(user_input1) == 1:
#         print('Paper ties with Paper')
#     elif int(user_input1) == 2:
#         print('Scissors beats Paper. You Win!!')
# elif computer_choice == 2:
#     if int(user_input1) == 0:
#         print('Rock beats Scissors. You Win!!')
#     elif int(user_input1) == 1:
#         print('Scissors beats Paper. You Lose!!')
#     elif int(user_input1) == 2:
#         print('Scissors ties with Scissors')











