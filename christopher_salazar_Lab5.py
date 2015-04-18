# christopher_salazar_Lab5.py
# Name: Christopher Salazar
# Date: 03/04/2015
# This program is a game where user will attempt to guess program's number.

# Import Modules
import random


# Main function
def main():
    computer_Number=0
    proceed=1
    try_again=1
    while proceed==1:
        print('Welcome to the guessing game! Try your luck and \
see if you can guess the number the computer is thinking!\n')
        input('Press ENTER to begin.\n')
        computer_Number= random.randint(1, 1000) #Random generator
       
        proceed=guess(computer_Number,proceed,try_again) # Calls Guess function
    #When proceed=0, the next two statements will exit program.            
    print('Thanks for playing!!!')
    exit()


# Guess function compares user guess to computer number.    
def guess(computer_Number,proceed,try_again):
    number_Tries=0
    user_Number=int(input('Guess a number between 1-1000: ')) #User Guess    
    while proceed==1:        
        if user_Number==computer_Number:
            number_Tries+=1
            print('\nYou guessed the correct number! Number of Tries: ',number_Tries)
            x=int(input('\nPress 1 and enter to play again.  Enter 2 to quit: '))
            if x==1:
                return 1
            else:
                return 0
        elif user_Number>=computer_Number-10 and user_Number<computer_Number:
            number_Tries+=1
            print('Getting warm but still low!\n')
            print('\nTimes Guessed: ',number_Tries)
            user_Number=int(input('\nGuess a number between 1-1000: '))
        elif user_Number<computer_Number and user_Number>0:
            number_Tries+=1
            print('Too Low!\n')
            print('Times Guessed: ',number_Tries)
            user_Number=int(input('\nGuess a number between 1-1000: '))
        elif user_Number<=computer_Number+10 and user_Number>computer_Number:
            number_Tries+=1
            print('Getting warm but still high!\n')
            print('Times Guessed: ',number_Tries)
            user_Number=int(input('\nGuess a number between 1-1000: '))
        elif user_Number>computer_Number and user_Number<1000:
            number_Tries+=1
            print('Too High!\n')
            print('Times Guessed: ',number_Tries)
            user_Number=int(input('\nGuess a number between 1-1000: '))
        else:
            print('Invalid number: please enter a number between 1-1000')
            user_Number=int(input('\nGuess a number between 1-1000: '))

#Call Main Function        
main()
