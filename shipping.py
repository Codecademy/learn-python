weight = 41.5

#Ground Shipping
flat_charge = 20

if weight <= 2:
  cost_ground = weight * 1.5 + flat_charge
elif weight > 2 and weight <= 6:
  cost_ground = weight *3 + flat_charge
elif weight > 6 and weight <= 10:
  cost_ground = weight * 4 + flat_charge
else:
  cost_ground = weight * 4.75 + flat_charge

print (f"Ground shipping cost: ${cost_ground:.2f}")

#Ground Shipping Premium
cost_ground_premium = 125.00
print (f"Ground shipping Premium cost: ${cost_ground_premium:.2f}")

#Drone Shipping
if weight <= 2:
  cost_drone = weight * 4.5
elif weight > 2 and weight <= 6:
  cost_drone = weight * 9
elif weight > 6 and weight <= 10:
  cost_drone = weight * 12
else:
  cost_drone = weight * 14.25

print (f"Drone shipping cost: ${cost_drone:.2f}")


