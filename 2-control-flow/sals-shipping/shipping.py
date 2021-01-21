# Sal's Shipping
# Sonny Li

weight = 80

# Ground Shipping 🚚

if weight <= 2:
  cost_ground = weight * 1.5 + 20
elif weight <= 6:
  cost_ground = weight * 3.00 + 20
elif weight <= 10:
  cost_ground = weight * 4.00 + 20
else:
  cost_ground = weight * 4.75 + 20

# Ground Shipping Premimum 🚚💨

cost_ground_premium = 125.00

# Drone Shipping 🛸

if weight <= 2:
  cost_drone = weight * 4.5
elif weight <= 6:
  cost_drone = weight * 9.00
elif weight <= 10:
  cost_drone = weight * 12.00
else:
  cost_drone = weight * 14.25

# This makes it easier for the customer to find the cheapest price quickly, while letting them see all their options
print("Your cheapest price is $" + min(str(cost_ground), str(cost_ground_premium), str(cost_drone)))
print(" ")
print("Ground shipping: $" + str(cost_ground))
print("Premium ground shipping: $" + str(cost_ground_premium))
print("Drone shipping: $" + str(cost_drone))
