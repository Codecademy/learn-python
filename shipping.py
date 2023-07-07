weight = 0
cost_ground = 20.00
cost_drone = 0.00
#Ground Shipping
if weight <= 2:
  cost_ground = weight * 1.50 + 20
elif weight <= 6:
  cost_ground = weight * 3 + 20
elif weight <= 10:
  cost_ground = weight * 4 + 20
else:
  cost_ground = weight * 4.75 + 20

print('Ground shipping cost: $', cost_ground)

#Ground Shipping Premium

print('Ground shipping premium cost: $ 125.00')

#Drone Shipping
if weight <= 2:
  cost_drone = weight * 4.50
elif weight <= 6:
  cost_drone = weight * 9
elif weight <= 10:
  cost_drone = weight * 12
else:
  cost_drone = weight * 14.25

print('Ground shipping cost: $', cost_drone)

#Suggestion
print('\n')
if cost_ground < 125.0 and cost_ground < cost_drone:
  print('Recomended option: Ground Shipping')
if cost_ground == 125.0 and cost_drone == 125.0:
  print('Recomended option: Ground Shipping / Ground Shipping premium / Drone Shipping')
if cost_ground > 125.0 and cost_drone > 125.0:
  print('Recomended option: Ground Shipping Premium')
if cost_drone < 125.0 and cost_ground > cost_drone:
  print('Recomended option: Drone Shipping')
