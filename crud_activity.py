# Step 1
# empty list to store recipes
cookbook = []

# Step 2
# function to read a recipe by index
def create(recipe):
    cookbook.append(recipe)
    print (f"Adding recipe: {recipe}")

# Step 3
# function to update a recipe by index & check if index is valid
def read(index):
    if index < len(cookbook):
        print (f"recipe at index {index}: {cookbook[index]}")
    else:
        print ("Index is out of range.")

# Step 4
# updates a recipe at a given index
def update(index, recipe):
    if index < len(cookbook):
        cookbook[index] = recipe
        print(f"Updated recipe at index {index} to: {recipe}")
    else:
        print("Index is out of range.")

# Step 5
# deletes a recipe at a given index
def destroy(index):
    if index < len(cookbook):
        print (f"Deleting recipe at index {index}: {cookbook[index]}")
        del cookbook[index]
    else: 
        print("Index is out of range.")

# Step 6
def list_all_recipes():
    print("Listing all recipes:")
    print(cookbook)


# additional imports
def main():
    while True:
        print("\nCookbook Recipes")
        print("1. Add a Recipe")
        print("2. Read a Recipe")
        print("3. Update a Recipe")
        print("4. Delete a Recipe")
        print("5. Display all Recipes")
        print("6. Exit")


        choice = input("Choose an option (1-6): ")


        if choice == "1":
            recipe = input("Enter the name of the recipe: ")
            create(recipe)
        elif choice == "2":
            index = input("Enter the index of the recipe to read: ")
            index = int(index)
            read(index)
        elif choice == "3":
            index = input("Enter the index of the recipe to update: ")
            recipe = input("Enter the name of the recipe you want to update it with: ")
            index = int(index)
            update(index, recipe)
        elif choice == "4":
            index = input("Enter the index of the recipe to delete: ")
            index = int(index)
            destroy(index)
        elif choice == "5":
            list_all_recipes()
        elif choice == "6":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")


main()
