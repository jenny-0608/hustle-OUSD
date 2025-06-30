
# Task 1: using a while loop to check if a user wants to continue checking if their eligible to vote
checking = "yes"
while checking == "yes":
    user_age = input("Enter your age: ")
    if int(user_age) >= 18:
        print("You are eligible to vote!")
        checking = input("would you like to check again? (yes/no): ")
    else:
        print("You are not eligible to vote.")
        checking = input("would you like to check again? (yes/no): ")



#Task 2

## This code iterates through a list of items in an inventory and performs actions based on the item.
inventory = ["tnt", "glass", "grass", "netherite", "waxed lightly weathered chiseled copper stairs"]
list_length = len(inventory)

# Iterate through the inventory and check each item
for i in inventory:
    if i == "waxed lightly weathered chiseled copper stairs":
        print(f"Why do you have {i} in your inventory??")
    elif i == "tnt":
        print(f"you got {i}? go bomb johnnys house!")
    else:
        print(f"nice {i}!! This is a valid item.")

# Task 3

number_list = [-8, -4, -2, 0, 1, 3, 5]

for i in number_list:
    if i > 0:
        print(f"{i} is a positive number.")
    elif i < 0:
        print(f"{i} is a negative number.")
    else:
        print("the number is zero!!")