# Sal's Shipping

weight = float(input("What is your weight? "))
cost_ground = 0
cost_drone = 0
ground_flat_charge = 20

# Ground Shipping

if weight <= 2:
  cost_ground += (weight * 1.50) + ground_flat_charge
elif 2 < weight <= 6:
  cost_ground += (weight * 3.00) + ground_flat_charge
elif 6 < weight <= 10:
  cost_ground += (weight * 4.00) + ground_flat_charge
elif weight > 10:
  cost_ground += (weight * 4.75) + ground_flat_charge
      
# Ground Shipping Premimum

cost_prem = 125.00

# Drone Shipping

if weight <= 2:
  cost_drone += (weight * 4.50)
elif 2 < weight <= 6:
  cost_drone += (weight * 9.00)
elif 6 < weight <= 10:
  cost_drone += (weight * 12.00)
elif weight > 10:
  cost_drone += (weight * 14.25)

# Output

if cost_ground < cost_drone and cost_ground < cost_prem:
  print("According to your luggage weight, the best plan our company recommends to use is the Ground Shipping Plan with a net charge of:", cost_ground, "\n\nBelow is a list of the cost of the service for each plan: \n1- Ground Shipping Plan:", cost_ground, "\n2- Ground Shipping Premium Plan:", cost_prem, "\n3- Drone Shipping Plan:", cost_drone, "\n\nThanks a lot for considering our company!")
elif cost_drone < cost_ground and cost_drone < cost_prem:
  print("According to your luggage weight, the best plan our company recommends to use is the Drone Shipping Plan with a net charge of:", cost_drone, "\n\nBelow is a list of the cost of the service for each plan: \n1- Ground Shipping Plan:", cost_ground, "\n2- Ground Shipping Premium Plan:", cost_prem, "\n3- Drone Shipping Plan:", cost_drone, "\n\nThanks a lot for considering our company!")
elif cost_prem < cost_ground and cost_prem < cost_drone:
  print("According to your luggage weight, the best plan our company recommends to use is the Ground Shipping Premium Plan with a net charge of:", cost_prem, "\n\nBelow is a list of the cost of the service for each plan: \n1- Ground Shipping Plan:", cost_ground, "\n2- Ground Shipping Premium Plan:", cost_prem, "\n3- Drone Shipping Plan:", cost_drone, "\n\nThanks a lot for considering our company!")
