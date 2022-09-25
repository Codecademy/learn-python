weight = 12

# Ground Shipping 

if weight <= 2:
  cost_ground = weight * 1.5 + 20
elif weight <= 6:
  cost_ground = weight * 3.00 + 20
elif weight <= 10:
  cost_ground = weight * 4.00 + 20
else:
  cost_ground = weight * 4.75 + 20

print("Ground Shipping: $", cost_ground)
      
# Ground Shipping Premimum 

cost_ground_premium = 125.00

print("Ground Shipping Premimium: $", cost_ground_premium)

# Drone Shipping 

if weight <= 2:
  cost_drone = weight * 4.5
elif weight <= 6:
  cost_drone = weight * 9.00
elif weight <= 10:
  cost_drone = weight * 12.00
else:
  cost_drone = weight * 14.25

print("Drone Shipping: $", cost_drone)

#The cheapest way to ship your package is ..

if cost_ground < cost_ground_premium and cost_ground < cost_drone:
 print ("The cheapest way to ship your package is", "Ground Shipping: $", cost_ground)
if cost_drone < cost_ground_premium and cost_drone < cost_ground:
 print ("The cheapest way to ship your package is", "Drone Shipping: $", cost_drone )
if cost_ground_premium < cost_ground and cost_ground_premium < cost_drone:
 print ("The cheapest way to ship your package is", "Ground Shipping Premimium: $", cost_ground_premium) 

