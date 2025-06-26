
#? what are sequence types?
# * ordered collections of items of some data types/types accessed via an index

hobbies = [ "rhythm+", "badminton", "hanging out with friends"]  # list of strings
#              0           1                 2            (when starting from front of the list)
#              -3          -2                -1           (when starting from back of the list)

print(hobbies[2])  # prints "hanging out with friends"
print(hobbies[-3])  # prints "rhythm+"

test = "word"
hassan = "idk"
#   print(test + " " +hassan)


numbs = [1, 2, 5, 6, 7]  # list of integers
# gonna use append
numbs.append(9)  # adds 9 to the end of the list

numbs.extend([10, 11])  # adds 10 and 11 to the end of the list
# gonna use extend
# difference between append and extend:
# append adds a single element to the end,  extend adds multiple elements from an iterable (like a list)

numbs.insert(2, 3) # inserts 3 at index 2
print (numbs)  # prints [1, 2, 3, 5, 6, 7, 9, 10, 11]


ex = ("blue", "cat", "johnny", "red", "green") # tuple of strings
# tuples are immutable, meaning they cannot be changed after creation
print( '#'.join(ex)) # example of adding something/nothing between the strings in ex

print (f"here is a string, {hassan}") # f is used to format strings, allowing for variable to be included in the string
ex_nd = ["blue", "cat", "johnny", "red", "green"]  # list of strings
ex_nd.remove("cat")
ex_nd.pop(1)  # removes the element at index 1, which is "johnny"
print(ex_nd)  # prints ['blue', 'johnny', 'red', 'green']
