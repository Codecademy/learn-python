weight = 41.5

# Ground Shipping

cost_ground_shipping = 0
cost_ground_shipping_premium = 125

if (weight <= 2):
    cost_ground_shipping = weight * 1.50 + 20.00
elif (weight <= 6):
    cost_ground_shipping = weight * 3.00 + 20.00
elif (weight <= 10):
    cost_ground_shipping = weight * 4.00 + 20.00
else:
    cost_ground_shipping = weight * 4.75 + 20.00

print("Ground Shipping $" + str(cost_ground_shipping))
print("Ground Shipping Premium $" + str(cost_ground_shipping_premium) + "\n")

# Drone Shipping

cost_drone_shipping = 0

if (weight <= 2):
    cost_drone_shipping = weight * 4.50
elif (weight <= 6):
    cost_drone_shipping = weight * 9.00
elif (weight <= 10):
    cost_drone_shipping = weight * 12.00
else:
    cost_drone_shipping = weight * 14.25

print("Drone Shipping $" + str(cost_drone_shipping))
