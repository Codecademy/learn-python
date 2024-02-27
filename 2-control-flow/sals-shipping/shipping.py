# Sal's Shipping
# Sonny Li

weight = 1.5
cost_ground = 0
cost_ground_premium = 125
cost_drone = 0

if weight <= 2:
  cost_ground = weight * 1.5 + 20
  cost_drone = weight * 4.5
elif weight <= 6:
  cost_ground = weight * 3 + 20
  cost_drone = weight * 9
elif weight <= 10:
  cost_ground = weight * 4 + 20
  cost_drone = weight * 12
else:
  cost_ground = weight * 4.75  + 20
  cost_drone = weight * 14.25

print(f"Ground shipping standard: {cost_ground}")
print(f"Drone shipping: {cost_drone}")
print(f"Ground premium cost: {cost_ground_premium}")
