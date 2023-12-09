weight = 1.50
# Ground Shipping
price_per_pound = ""
flat_charge = 20.00
if weight >= 0.01 and weight <= 2.00:
  price_per_pound = 1.50
elif weight >= 2.00 and weight <= 6.00:
  price_per_pound = 3.00
elif weight >= 6.00 and weight <= 10.00:
  price_per_pound = 4.00
elif weight >= 10.00:
  price_per_pound = 4.75
else:
  print("Error: specify the weight")
cost_ground = weight * price_per_pound
print("Ground Cost $ " , flat_charge + cost_ground)
#Ground Shipping Premium
cost_ground_premium = 125.00
print("Ground Shipping Premium $ " + str(cost_ground_premium))
#Drone Shipping
price_per_pound_drone = ""
if weight >= 0.00 and weight <= 2.00:
  price_per_pound_drone = 4.50
elif weight >= 2.00 and weight <= 6.00:
  price_per_pound_drone = 9.00
elif weight >= 6.00 and weight <= 10.00:
  price_per_pound_drone = 12.00
elif weight >= 10.00:
  price_per_pound_drone = 14.25
else:
  print("Error")
cost_ground_drone = weight * price_per_pound_drone
print("Ground Drone Cost $ " ,cost_ground_drone)
