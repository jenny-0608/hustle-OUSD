# Lab 3

# Task 1: working with variables
food = "ceviche de camaron"
# slice the string to get the first three characters only
print("our first three characters: " + food[0:3])  # Output: cev
print("our last three characters: " + food[-3:])  # Output: ron
# if going to the end of a string, you can omit the index

first_last = food[0] + food[-1]
print("first and last characters: " + first_last)  # Output: 'cn'

# split the string into a list of words
food_list = food.split()
print(food_list)

# join all words togther with a space
joined_food = " ".join(food_list)
print(joined_food)  # Output: 'ceviche de camaron'

# Task 2: working with lists
number_list = [1, 18, 32, -5, 0, 234]

number_list.append(100) # Append 100 to the end of the list
number_list.insert(3, 25) # Insert 25 at index 3
number_list.pop (-1) # Remove the last element of the list
number_list.remove(number_list[1]) # Remove the first occurrence of 32 which is at index 2
print(number_list)  # Output: [1, 18, 25, -5, 0, 234]

# slicing number list
print(number_list[0:3])  # Output: [1, 18, 25]
print(number_list[-3:])  # Output: [-5, 0, 234]

# Task 3: working with dictionaries
books = {"R.F Kuang": "The Poppy War", "George Orwell": "Animal Farm", "Osumu Dazai": "No Longer Human", "Justina Ireland": "Dread Nation"}
print(books.keys()) # should show the keys of the dictionary
print(books.values())  # should show the values of the dictionary
print(books.get("Osumu Dazai"))  # should show the value of the key at index 2
books.pop("George Orwell")  # remove the key-value pair for George Orwell
print (books)  # should show the dictionary without George Orwell
del books["R.F Kuang"]  # delete the key-value pair for R.F Kuang
print(books)  # should show the dictionary without R.F Kuang