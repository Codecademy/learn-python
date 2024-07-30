# Sal's Shipping
# Sonny Li

weight = 80

# Ground Shipping 🚚

if weight <= 2:
  cost_ground = weight * 150 + 20
elif weight <= 6:
  cost_ground = weight * 300 + 20
elif weight <= 10:
  cost_ground = weight * 400 + 20
else:
  cost_ground = weight * 475 + 20

print("Ground Shipping:", cost_ground + '¢')
      
# Ground Shipping Premimum 🚚💨

cost_ground_premium = 12500

print("Ground Shipping Premimium:", cost_ground_premium + '¢')

# Drone Shipping 🛸

if weight <= 2:
  cost_drone = weight * 450
elif weight <= 6:
  cost_drone = weight * 900
elif weight <= 10:
  cost_drone = weight * 1200
else:
  cost_drone = weight * 1425

print("Drone Shipping:", cost_drone + '¢')
