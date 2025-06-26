
# Step 1
menu = {'Pizza': 2.99, 'Burger': 3.99, 'Hot dog': 1.99, 'Cheese': 0.59, 'Ice cream': 1.49, 'Churro': 0.79, 'Soda': 0.89}


# Step 2
def total_price(order1, order2) :
    order1 = menu.get(order1)
    order2 = menu.get(order2)
    total_sum = order1 + order2
    return total_sum

order1 = input ("Enter first order: ")
order2 = input ("Enter second order: ")

if order1 not in menu or order2 not in menu:
    print("One or both of the orders are not on the menu.")
else:
    print( f"The total price for {order1} and a(n) {order2} is: $", total_price(order1, order2) )   # Output should be the sum of the prices of the two items


# Step 3
def price_difference(order1, order2):
    order1 = menu.get(order1)
    order2 = menu.get(order2)
    total_difference = order1 - order2

    if total_difference < 0:
        total_difference = order2 - order1
    else:
        total_difference = order1 - order2
        
    return total_difference

order1 = input ("Enter first order: ")
order2 = input ("Enter second order: ")

if order1 not in menu or order2 not in menu:
    print("One or both of the orders are not on the menu.")
else:
    print( f"The price difference between {order1} and a(n) {order2} is: $", price_difference(order1, order2) )


# Step 4
def inflation(order):
    order = menu.get(order)
    inflation_price = round(order * 1.03, 2)
    inflation_menu = {item: round(price * 1.03, 2) for item, price in menu.items()} # Create a new dictionary with inflated prices
    return inflation_price, inflation_menu

order = input("Enter an order to check the inflation prices: ")

if order not in menu:
    print("the order is not in the menu! Try another.")
else:
    print("The new menu with inflation prices is:", inflation(order)[1])
    print( f"The inflation price for {order} is: $", inflation(order)[0] )


# Step 5
def deflation(order):
    order = menu.get(order)
    deflation_price = round(order * 0.97, 2)
    deflation_menu = {item: round(price * 0.97, 2) for item, price in menu.items()} # Create a new dictionary with deflated prices
    return deflation_price, deflation_menu

order = input("Enter an order to check the deflation prices: ")

if order not in menu:
    print("the order is not in the menu! Try another.")
else:
    print("The new menu with deflation prices is:", deflation(order)[1])
    print( f"The deflation price for {order} is: $", deflation(order)[0] )


# Step 6
def food_budget(order, budget):
    order_price = menu.get(order)

    if order_price is None:
        return "The order is not on the menu."
    if order_price <= budget:
        return f"You can afford {order} with your budget of ${budget}."
    else:
        return f"You are over budget for this order."

budget = float(input("Enter your budget: "))
order = input("Enter an order to check if you can afford it: ")

print(food_budget(order, budget))
