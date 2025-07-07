 # lab 5 Jannifer Calmo

# Step 1: cat fucntion
def cat_greeting(word):
    print(f"cat says {word}")

cat_greeting("meow")

# Step 2: superhero power function
def generate_superhero_power():
    name = "Johnny"
    power = "flying"
    print(f"{name}'s superhero power is {power}")

generate_superhero_power()

# step 3:
def generate_superhero_power1():
    power = "Flying"
    return power

print(generate_superhero_power1())

# Step 4

def generate_superhero_power2(user_name, super_power):
    message = user_name + " has the super power of " + super_power + "!"
    return message

print(generate_superhero_power2("Jannifer", "teleportation"))

# Step 5
def cat_greetings_loop(greeting):
    for i in range(5):
        print(f"cat says {greeting}")

cat_greetings_loop("meow")

# another way
def cat_greeting_loop2():
    greetings = ["purr", "screech", "hiss", "mew", "yowl"]
    for i in greetings:
        print(f"cat says {i}")

cat_greeting_loop2()

def generate_multiple_powers():
    super_powers = ["flying", "invisibility", "teleportation", "time travel"]
    for i in super_powers:
        print(f"you have the power of {i}")

generate_multiple_powers()