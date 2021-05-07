#Sal's Shipping
#Ilona Louckova

weight = 80

#Ground Shipping
ground_flat = 20.00
if weight <= 2:
  gs_pp = 1.50
elif weight <= 6:
  gs_pp = 3.00
elif weight <= 10:
  gs_pp = 4.00
else:
  gs_pp = 4.75
cost_ground = weight * gs_pp + ground_flat
print ("Ground Shipping $", cost_ground)

#Ground Shipping Premium
cost_premium = 125.00
print ("Ground Shipping Premium $", cost_premium)

#Drone Shipping
if weight <= 2:
  ds_pp = 4.50
elif weight <= 6:
  ds_pp = 9.00
elif weight <= 10:
  ds_pp = 12.00
else:
  ds_pp = 14.25
cost_drone = weight * ds_pp
print ("Drone Shipping $", cost_drone)
