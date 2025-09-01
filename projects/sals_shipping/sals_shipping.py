# Sal's Shipping Calculator
# This script calculates shipping costs for Ground, Premium Ground, and Drone shipping based on package weight.
# Author: Daniel Veloso
# Date: September 1, 2025

weight = 41.5  # Weight of the package in kg, used as a fixed example

# Calculate Ground Shipping cost
# Base fee is $20, with additional rates per kg based on weight ranges
if weight <= 2:
    cost_ground = 20 + 1.5 * weight  # Up to 2 kg: $1.50 per kg
elif weight <= 6:
    cost_ground = 20 + 3 * weight    # 2-6 kg: $3.00 per kg
elif weight <= 10:
    cost_ground = 20 + 4 * weight    # 6-10 kg: $4.00 per kg
else:
    cost_ground = 20 + 4.75 * weight # Above 10 kg: $4.75 per kg

print("Cost for Ground Shipping: $" + str(cost_ground))  # Output the calculated cost

# Calculate Premium Ground Shipping cost
# Fixed rate of $125.00 regardless of weight
cost_premium_ground = 125.00
print("Cost for Premium Ground Shipping: $" + str(cost_premium_ground))  # Output the fixed cost

# Calculate Drone Shipping cost
# No base fee, with rates per kg based on weight ranges
if weight <= 2:
    cost_drone = 4.5 * weight  # Up to 2 kg: $4.50 per kg
elif weight <= 6:
    cost_drone = 9 * weight    # 2-6 kg: $9.00 per kg
elif weight <= 10:
    cost_drone = 12 * weight   # 6-10 kg: $12.00 per kg
else:
    cost_drone = 14.25 * weight # Above 10 kg: $14.25 per kg

print("Cost for Drone Shipping: $" + str(cost_drone))  # Output the calculated cost