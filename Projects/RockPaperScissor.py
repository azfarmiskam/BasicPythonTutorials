#!/usr/bin/env python3

import random
import os
import re
import time

os.system('cls' if os.name=='nt' else 'clear')
userScore = int(0)
compScore = int(0)

while True:

    if userScore == 5 or compScore == 5:
        print("----------\n")
        print('Game End')
        time.sleep(2)
        print('Final Score is You [{}]'.format(userScore) + " and Computer [{}]".format(compScore))
        if userScore < compScore:
            time.sleep(0.6)
            print("----------\n")
            print("You LOSE!")
            print("\n----------")
        else:
            time.sleep(0.6)
            print("**********\n")
            print("You WIN!")
            print("\n**********")
        time.sleep(2)
        break

    time.sleep(0.5)
    print("----------\n")
    print("Current Score" )
    print("You [{}]".format(userScore) + " : Computer [{}]".format(compScore))
    print("\n----------")
    time.sleep(1)
    print("Rock, Paper, Scissors - Shoot!")
    userChoice = input("Choose your weapon [R]ock], [P]aper, or [S]cissors: ")

    if not re.match("[SsRrPp]", userChoice):
        print("Please choose a letter:")
        print("[R]ock, [S]cissors or [P]aper.")
        continue

    time.sleep(1)
    print("You chose: " + userChoice)
    choices = ['R', 'P', 'S']
    ComputerChoice = random.choice(choices)
    print("I chose: " + ComputerChoice)
    print('----------')

    if ComputerChoice == str.upper(userChoice):
        time.sleep(0.5)
        print("Tie! ")
        time.sleep(0.5)

    elif ComputerChoice == 'R' and userChoice.upper() == 'S':
        time.sleep(0.5)
        print("Scissors beats rock, I win! ")
        time.sleep(0.5)
        compScore += 1
        continue

    elif ComputerChoice == 'S' and userChoice.upper() == 'P':
        time.sleep(0.5)
        print("Scissors beats paper! I win! ")
        time.sleep(0.5)
        compScore += 1
        continue

    elif ComputerChoice == 'P' and userChoice.upper() == 'R':
        time.sleep(0.5)
        print("Paper beat rock, I win!")
        time.sleep(0.5)
        compScore += 1
        continue

    else:
        time.sleep(0.5)
        print("You win!")
        time.sleep(0.5)
        userScore +=1