# Sal's Shipping
# Hugo

weight = float(input("Please type in the package weight: "))

# For maintenance purposes, we implement tables

# Ground shipping table
cost_ground_flat_charge = 20.00
cost_groud_2 = 1.50
cost_groud_2_6 = 3.00
cost_groud_6_10 = 4.00
cost_groud_10 = 4.75

#Ground shipping Premium
# no table. Flat Rate 

# Drone shipping table
cost_drone_flat_charge = 0.00
cost_drone_2 = 4.50
cost_drone_2_6 = 9.00
cost_drone_6_10 = 1.00
cost_drone_10 = 14.25

# Ground Shipping
if weight <= 2:
  cost_ground = weight * cost_groud_2 + cost_ground_flat_charge
elif weight > 2 and weight <= 6:
  cost_ground = weight * cost_groud_2_6 + cost_ground_flat_charge
elif weight > 6 and weight <= 10:
  cost_ground = weight * cost_groud_6_10 + cost_ground_flat_charge
else:
  cost_ground = weight * cost_groud_10 + cost_ground_flat_charge
print("Ground Shipping $ " + str(cost_ground))

# Ground Shipping Premium
cost_ground_premium = 125.00
print("Ground Shipping Premium $ " + str(cost_ground_premium))

# Drone Shipping
if weight <= 2:
  cost_drone = weight * cost_drone_2 + cost_drone_flat_charge
elif weight > 2 and weight <= 6:
  cost_drone = weight * cost_drone_2_6 + cost_drone_flat_charge
elif weight > 6 and weight <= 10:
  cost_drone = weight * cost_drone_6_10 + cost_drone_flat_charge
else:
  cost_drone = weight * cost_drone_10 + cost_drone_flat_charge

print("Drone Shipping $ " + str(cost_drone))
