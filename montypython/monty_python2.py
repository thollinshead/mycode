#!/usr/bin/env python3
# integer round initated to 0
round = 0
# set up infinite loop condition
while(True):
# increase round counter
    round = round + 1
    print('Finish the movie title, "Monty Python\'s The Life of _____"')
# logic to check correct answer no matter the case  
    answer = input()
    if (answer.lower() == 'brian'):
        print('Correct')
# break statement escapes the while loop        
        break
# logic to ensure round has not reached 3
    elif(round==3):
        print('Sorry, the answer was Brian.')
# break statement escapes the while loop
        break
# if answer was wrong, and round is not yet equal to 3
    else:
        print('Sorry! Try again!')
