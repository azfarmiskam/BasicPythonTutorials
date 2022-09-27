# Variable - List

Lists are used to store multiple items in a single variable.

List items are ordered, changeable, and allow duplicate values.

Similarly to Array, list items are indexed, the first item has index `[0]`, the second item has index `[1]` etc.

When we say that lists are ordered, it means that the items have a defined order, and that order will not change.

If you add new items to a list, the new items will be placed at the end of the list.

The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

Use square brackets \[ ]

```python
#Example 1

list1 = ['Alia', 'Yusof', 23, 24]
list2 = ["apple", "cherry", "orange"]
list3 = [1, 2, 3, 4, 5]
thislist = ["apple", "banana", "cherry", "apple", "cherry"]

```

## Accessing Item in List

Exercise #1: Creating List

{% code overflow="wrap" %}
```python

list1 = ["apple", "grape", "orange", "banana", "strawberry"]

print (list1)
```
{% endcode %}

Output: `['apple', 'grape', 'orange', 'banana', 'strawberry']`

\-------------------------------------------

Exercise #2: Indexing

```python
print (list1[0]) #return item with index 0
print (list1[1]) #return item with index 1
print (list1[3]) #return item with index 3
```

Output:  `apple`\
&#x20;             `grape`\
&#x20;             `banana`

\--------------------------------------------

Exercise #3: Slicing and Range Indexing

```python
print (list1[:0]) #first 0 item start with index 0
print (list1[:2]) #first 2 items start with index 0
print (list1[2:4]) #first 4 items but skip 2 items
```

Output:   `[]`\
&#x20;               `['apple', 'grape']`\
&#x20;               `['orange', 'banana']`

&#x20; \--------------------------------------------

Exercise #4: Last Item

```python
print (list1[-1]) #return last item
print (list1[-2]) #return second last item
print (list1[-2:]) #return 2 last items
```

Output:

`strawberry`\
`banana`\
`['banana', 'strawberry']`

&#x20;\--------------------------------------------

Exercise #5: Change Item Value

```python
list1[2] = "guava" #change item at index 2
print (list1)
```

Output: `['apple', 'grape', 'guava', 'banana', 'strawberry']`

\--------------------------------------------

Exercise #6: Delete Item Value

```python
del list1[2] #delete item at index 2
print (list1)
```

Output:

`['apple', 'grape', 'banana', 'strawberry']`

\--------------------------------------------

Exercise #7: Add Item Value

```python
list1.append('pineapple') #add item at the end of list
print (list1)

list1.insert(1, 'mango') #insert new item at index 1
print (list1)
```

Output:

`['apple', 'grape', 'banana', 'strawberry', 'pineapple']`\
`['apple', 'mango', 'grape', 'banana', 'strawberry', 'pineapple']`

## List Methods



| Method    | Description                                                                  |
| --------- | ---------------------------------------------------------------------------- |
| append()  | Adds an element at the end of the list                                       |
| clear()   | Removes all the elements from the list                                       |
| copy()    | Returns a copy of the list                                                   |
| count()   | Returns the number of elements with the specified value                      |
| extend()  | Add the elements of a list (or any iterable), to the end of the current list |
| index()   | Returns the index of the first element with the specified value              |
| insert()  | Adds an element at the specified position                                    |
| pop()     | Removes the element at the specified position                                |
| remove()  | Removes the item with the specified value                                    |
| reverse() | Reverses the order of the list                                               |
| sort()    | Sorts the list                                                               |

