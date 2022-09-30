# Guessing Number

{% embed url="https://github.com/azfarmiskam/PythonBasic_Tutorials/blob/main/Projects/GuessingGame.py" %}

This project is a fun game that generates a random number in a certain specified range and the user must guess the number after receiving hints. Every time a user’s guess is wrong they are prompted with more hints to make it easier — at the cost of reducing the score.

The program also requires functions to check if an actual number is entered by the user, and finds the difference between the two numbers.&#x20;

{% code title="GuessingNumber.py" %}
```python
#!/usr/bin/env python3

import random
import time
attempts_list = []

def show_score():
    if len(attempts_list) <= 0:
        time.sleep(1)
        print("There is currently no high score, it's yours for the taking!")
        print('---------')
    else:
        time.sleep(1)
        print("The current high score is {} attempts".format(min(attempts_list)))
        print('---------')

def start_game():
    random_number = int(random.randint(1, 10))
    print(' ')
    print('******* WELCOME *******')
    print(' ')
    print("Hello traveler! Welcome to the game of guesses!")
    print(' ')
    print('---------')
    time.sleep(1)
    player_name = input("What is your name? ")
    print('---------')
    time.sleep(0.5)
    wanna_play = input("Hi, {}, would you like to play the guessing game? (Enter Yes/No) ".format(player_name))
    print('---------')

# Where the show_score function USED to be

    attempts = 0
    show_score()
    while wanna_play.lower() == "yes" or "y":
        try:
            time.sleep(1)
            print('Attempts : #' + str(attempts+1))
            time.sleep(1)
            guess = input("Pick a number between 1 and 10 ")
            if int(guess) < 1 or int(guess) > 10:
                raise ValueError("Please guess a number within the given range")

            if int(guess) == random_number:
                print("Nice! You got it!")
                attempts += 1
                attempts_list.append(attempts)
                print('---------')
                time.sleep(1)
                print("It took you {} attempts".format(attempts))
                print('---------')
                play_again = input("Would you like to play again? (Enter Yes/No) ")
                attempts = 0
                show_score()
                random_number = int(random.randint(1, 10))

                if play_again.lower() == "no":
                    time.sleep(1)
                    print("Ok! See you again {}".format(player_name))
                    print('Bye Bye')
                    
                    break

            elif int(guess) > random_number:
                print('---------')
                print("It's lower")
                attempts += 1

            elif int(guess) < random_number:
                print('---------')
                print("It's higher")
                attempts += 1

        except ValueError as err:
            print("Oh no!, that is not a valid value. Try again...")
            print("({})".format(err))
            print('---------')
        else:
            print("That's cool, try again!")
            print('---------')
            time.sleep(1)

if __name__ == '__main__':
    start_game()
```
{% endcode %}
