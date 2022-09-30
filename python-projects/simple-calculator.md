# Simple Calculator

{% embed url="https://github.com/azfarmiskam/PythonBasic_Tutorials/blob/main/Projects/SimpleCalculator.py" %}

{% code title="SimpleCalculator.py" %}
```python
#!/usr/bin/env python3

import time

def addition():
    n = float(input("Enter the number: "))
    t = 0  #Total number enter
    ans = 0
    while n != 0:
        ans = ans + n
        t += 1
        n = float(input("Enter another number (0 to calculate): "))
    return [ans, t]

def subtraction():
    n = float(input("Enter the number: "))
    t = 0  #Total number enter
    ans = n
    while n != 0:
        t += 1
        n = float(input("Enter another number (0 to calculate): "))
        ans = ans - n
    return [ans, t]

def multiplication():
    n = float(input("Enter the number: "))
    t = 0  #Total number enter
    ans = 1

    while n != 0:
        ans = ans * n
        t += 1
        n = float(input("Enter another number (0 to calculate): "))
    return [ans, t]

def divide():
    n = float(input("Enter the first number: "))
    k = float(input("Enter the second number: "))
    ans = n/k
    return [ans]

def average():
    an = []
    an = addition()
    t = an[1]
    a = an[0]
    ans = a / t
    return [ans, t]

while True:
    list = []
    print('-------------------')
    print(" Enter 'a' for addition")
    print(" Enter 's' for substraction")
    print(" Enter 'm' for multiplication")
    print(" Enter 'd' for division")
    print(" Enter 'v' for average")
    print(" Enter 'q' for quit")
    c = input("type your choice here :  ")

    if c != 'q':
        if c == 'a':
            print('Addition')
            list = addition()
            print("Ans = ", list[0], " total inputs ",list[1])
            time.sleep(0.5)

        elif c == 's':
            print("Subtraction")
            list = subtraction()
            print("Ans = ", list[0], " total inputs ",list[1])
            time.sleep(0.5)

        elif c == 'm':
            print("Multiplication")
            list = multiplication()
            print("Ans = ", list[0], " total inputs ",list[1])
            time.sleep(0.5)

        elif c == 'd':
            print("Division")
            list = divide()
            print("Ans = ", list[0],)
            time.sleep(0.5)

        elif c == 'v':
            print("Average Value of ...")
            list = average()
            print("Ans = ", list[0], " total inputs ",list[1])
            time.sleep(0.5)

        else:
            print ("Sorry, invalid character")

    else:
        break
```
{% endcode %}
