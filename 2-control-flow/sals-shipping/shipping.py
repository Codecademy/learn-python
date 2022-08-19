weight = 800.40

ground_price = None

drone_price = None

premium_flat_price = 125

#Ground
if weight <= 2:
  ground_price = weight * 1.5 + 20
elif weight > 2 and weight <= 6:
  ground_price = weight * 3 + 20
elif weight > 6 and weight <= 10:
  ground_price = weight * 4 + 20
elif weight > 10:
  ground_price = weight * 4.75 + 20

print("Ground price $", round(ground_price, 2))

#Drone
if weight <= 2:
  drone_price = weight * 4.5
elif weight > 2 and weight <= 6:
  drone_price = weight * 9
elif weight > 6 and weight <= 10:
  drone_price = weight * 12
elif weight > 10:
  drone_price = weight * 14.25

print("Drone price $", round(drone_price, 1))

cheapest_option = min(ground_price, drone_price, premium_flat_price)

if cheapest_option == ground_price:
  print("go with ground, it's $", round(ground_price))
elif cheapest_option == drone_price:
  print("go with the drone, it's $", round(drone_price, 2))
else:
  print("premium, baby")
