# Declare the varibles
weight = 41.5
cost_ground_premium = 125.00

# Determine the cost of Ground Shipping
if weight <= 2:
  cost_ground = weight * 1.5 + 20
elif weight <= 6:
  cost_ground = weight * 3.0 + 20
elif weight <= 10:
  cost_ground = weight * 4.0 + 20
else:
  cost_ground = weight * 4.75 + 20
print("Ground Shipping $", cost_ground)
print("Ground Shipping Premium $", cost_ground_premium)

# Determine the cost of Drone Shipping
if weight <= 2:
  cost_drone = weight * 4.5
elif weight <= 6:
  cost_drone = weight * 9.0
elif weight <= 10:
  cost_drone = weight * 12.0
else:
  cost_drone = weight * 14.25
print("Drone Shipping $", cost_drone)
