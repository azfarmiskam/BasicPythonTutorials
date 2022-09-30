# Binary Search Algorithm

{% embed url="https://github.com/azfarmiskam/PythonBasic_Tutorials/blob/main/Projects/BinarySearchAlgorithm.py" %}

The binary search algorithm is a very important one, and requires you to create a list of numbers between 0 and an upper limit, with every succeeding number having a difference of 2 between them.&#x20;

When the user inputs a random number to be searched the program begins its search by dividing the list into two halves. First, the first half is searched for the required number and if found, the other half is rejected and vice versa. The search continues until the number is found or the subarray size becomes zero.

{% code title="BinarySearchAlgorithm.py" %}
```python
#!/usr/bin/env python3

# Recursive Binary Search algorithm in Python
def binarySearch(array, x, low, high):
    if high >= low:
        mid = low + (high - low)//2
# If found at mid, return the value
        if array[mid] == x:
            return mid

# Search the first half
        elif array[mid] > x:
            return binarySearch(array, x, low, mid-1)

# Search the second half
        else:
            return binarySearch(array, x, mid + 1, high)

    else:
        return -1

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = int(input("Enter a number between 1 and 10:"))
result = binarySearch(array, x, 0, len(array)-1)


if result != -1:
    print("Element is present at position " + str(result))

else:
    print("Element not found")
```
{% endcode %}
