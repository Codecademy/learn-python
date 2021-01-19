weight_premium = 125
print("Ground Shipping Premium is $"+str(weight_premium))

def package(weight):
  if weight <= 2:
    cost_ground = weight * 1.50 + 20
    cost_drone = weight * 4.56
  elif weight <= 6:
    cost_ground = weight * 3.00 + 20
    cost_drone = weight * 9.00
  elif weight <= 10:
    cost_ground = weight * 4.00 + 20
    cost_drone = weight * 12.00
  elif weight > 10:
    cost_ground = weight * 4.75 + 20
    cost_drone = weight * 14.25
  else:
    print("None.")
  
  print("Ground Shipping is $"+str(cost_ground))
  print("Drone Shipping is $"+str(cost_drone))
  return

package(4.8)
