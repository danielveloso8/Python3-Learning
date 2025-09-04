# Carly's Clippers Revenue Calculator
# This script calculates average haircut prices, total revenue, and lists affordable cuts.
# Author: Daniel Veloso
# Date: September 1, 2025

# List of hairstyle types
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

# Corresponding prices for each hairstyle in dollars
prices = [30, 25, 40, 20, 20, 35, 50, 35]

# Number of haircuts sold for each style last week
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# Calculate total price for all hairstyles
total_price = 0
for price in prices:
    total_price += price  # Sum all prices

# Compute average price per haircut
average_price = total_price / len(prices)
print(f"Average Haircut Price: ${average_price:.2f}")  # Display with 2 decimal places

# Reduce each price by 5 dollars as per Carly's decision
new_prices = [price - 5 for price in prices]  # List comprehension for new prices
print(f"New Prices: {new_prices}")  # Updated prices after discount

# Calculate total revenue based on original prices and last week's sales
total_revenue = 0
for i in range(len(hairstyles)):
    total_revenue += prices[i] * last_week[i]  # Multiply price by number of cuts

print(f"Total Revenue: ${total_revenue}")  # Display total revenue

# Calculate average daily revenue (assuming 7 days in a week)
average_daily_revenue = total_revenue / 7
print(f"Average Daily Revenue: ${average_daily_revenue:.2f}")  # Display with 2 decimal places

# List hairstyles with new prices under $30
cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if new_prices[i] < 30]
print(f"Cuts Under $30: {cuts_under_30}")  # List of affordable hairstyles