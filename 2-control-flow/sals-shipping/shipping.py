#Sal's Shipping
#Sonny Li
#Ayodeji @dejisol

weight = 41.5
flat_charge = 20

# Ground Shipping 🚚

if weight <= 2:
  cost_ground = weight * 1.50 + flat_charge
elif weight <= 6:
  cost_ground = weight * 3.00 + flat_charge
elif weight <= 10:
  cost_ground = weight * 4.00 + flat_charge
elif weight > 10:
  cost_ground = weight * 4.75 + flat_charge
print("Ground Shipping Cost is $",cost_ground)
      
# Ground Shipping Premimum 🚚💨

cost_ground_premium = 125.00
print("Ground Premium Shipping cost is $",cost_ground_premium)

# Drone Shipping 🛸

if weight <= 2:
  cost_drone = weight * 4.50
elif weight <= 6:
  cost_drone = weight * 9.00
elif weight <= 10:
  cost_drone = weight * 12.00
elif weight > 10:
  cost_drone = weight * 14.25
print("Drone Shipping Cost is $",cost_drone)
