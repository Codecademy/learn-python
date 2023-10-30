weight = 1.5

# Ground Shipping

if weight <= 2:
  cost_ground = weight * 1.5 + 20
elif weight >= 2 and weight <= 6:
  cost_ground = weight * 3.0 + 20
elif weight >= 6 and weight <= 10:
  cost_ground = weight * 4.0 + 20
elif weight > 10:
  cost_ground = weight * 4.75 + 20

print("Weight of package: ", weight)
print("Cost of ground shipping: $", cost_ground)

cost_ground_premium = cost_ground + 125.00

print("Cost of ground shipping premium: $", cost_ground_premium)

# Drone Shipping

if weight <= 2:
  cost_drone = weight * 4.5
elif weight >= 2 and weight <= 6:
  cost_drone = weight * 9.0
elif weight >= 6 and weight <= 10:
  cost_drone = weight * 12 
elif weight > 10:
  cost_drone = weight * 14.25 

print("Cost of drone shipping: $", cost_drone)
