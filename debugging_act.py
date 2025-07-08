# debugging activity Jannifer Calmo

# case 1: 
# enocuntered a zerodivisionerror comes up when dividing by 0, fixed by dividing by 2
x = 10
y = 5
result = x / y
print("Result: ", result)

# case 2:
# list index was out of range, removed the + 1 in the print statement
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
    print(numbers[i])

# case 3:
# was a syntax error, needed to add a ":" to the function
def calculate_area(radius):
   area = 3.14 * radius ** 2
   return area
 
radius = 5
print(calculate_area(radius))

# case 4
# had two syntax errors for the if and else statement lines, added a ":" two both lines
def is_even(number):
   if number % 2 == 0:
       return True
   else:
       return False
 
print(is_even(4))
print(is_even(7))

# case 5 
# had a syntax error, added a ":" to the for loop
for i in range(5):
   print(i)

# case 6
# syntax error, needed a comma after the paranthesis but before name
def greet(name):
   return "Hello, ", name
 
print(greet("Alice"))

# case 7
# indentation error for the sum += number, added indentation
numbers = [1, 2, 3, 4, 5]
sum = 0
for number in numbers:
    sum += number
print("Sum of numbers:", sum)

# case 8
# changed the - sign to a +
def factorial(n):
   
   if n == 0:
       return 1
   else:
       return n * factorial(n-1) 
print(factorial(5))

# case 9
# would not print out hello stranger if name was not alice or bob, added anther name variable for bob
name = input("Enter your name: ")
if name == "Alice" or name == "Bob":
   print ("Hello, ", name)
else:
   print("Hello, stranger!")

# case 10
# has a zerodivisionerror, changed the 0 into a 10
def divide_numbers(x, y):
   result = x / y
   return result
 
num1 = 10
num2 = 10
print(divide_numbers(num1, num2))



