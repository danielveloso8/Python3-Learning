# Len's Slice Exercise
# This script manages a list of pizza toppings and prices, performing sorting and slicing operations.
# Author: Daniel Veloso
# Date: September 1, 2025

# Define lists of toppings and their prices
toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']
prices = [2, 6, 1, 3, 2, 7, 2]

# Count the number of $2 slices
num_two_dollar_slices = prices.count(2)  # Count occurrences of price 2

# Calculate total number of pizza types
num_pizzas = len(toppings)  # Total number of unique toppings

# Combine prices and toppings into a single list of lists
pizza_and_prices = [[2, 'pepperoni'], [6, 'pineapple'], [1, 'cheese'], [3, 'sausage'], 
                    [2, 'olives'], [7, 'anchovies'], [2, 'mushrooms']]

# Sort the list by price (ascending order)
pizza_and_prices.sort()  # Sorts based on the first element of each sublist (price)

# Find the cheapest pizza (first item after sorting)
cheapest_pizza = pizza_and_prices[0][1]  # Access the topping from the first sublist

# Find the priciest pizza (last item after sorting)
priciest_pizza = pizza_and_prices[-1][1]  # Access the topping from the last sublist

# Remove the last item (anchovies pizza) as it was sold
pizza_and_prices.pop()  # Removes the last sublist [7, 'anchovies']

# Add a new pizza type with price (intended as a single item, not a nested list)
pizza_and_prices.append([2.5, 'peppers'])  # Add peppers as a new pizza type

# Extract the three cheapest pizzas
three_cheapest_list = pizza_and_prices[:3]  # Slice the first three items
print("Three cheapest pizzas:", three_cheapest_list)  # Display the result