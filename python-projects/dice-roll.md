# Dice Roll

{% embed url="https://github.com/azfarmiskam/PythonBasic_Tutorials/blob/main/Projects/DiceRoll.py" %}

This dice roll generator is a fairly simple program that makes use of the random function to simulate dice rolls. You can change the maximum value to any number, making it possible to simulate polyhedral dice used in many board games and roleplaying games.

{% code title="DiceRoll.py" %}
```python
#!/usr/bin/env python3

import random

#Enter the minimum and maximum limits of the dice rolls below
min_val = 1
max_val = 6

#the variable that stores the user’s decision
roll_again = "yes"

#The dice roll loop if the user wants to continue
while roll_again == "yes" or roll_again == "y":
    print("Dices rolling...")
    print("The values are :")
#Printing the randomly generated variable of the first dice
    print(random.randint(min_val, max_val))
#Printing the randomly generated variable of the second dice
    print(random.randint(min_val, max_val))
#Here the user enters yes or y to continue and any other input ends the program
    roll_again = input("Roll the Dices Again?")
```
{% endcode %}
