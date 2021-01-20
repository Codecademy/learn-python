# Sal's Shipping
# Eleni A.

weight = 41.5
GS_FLAT = 20
GSP_FLAT = 125

#Basic Scale Shipping costs
def basic_shipping(weight):
  if weight <= 2:
    cost = weight * 1.50
  elif weight <= 6:
    cost = weight * 3
  elif weight <=10:
    cost = weight * 4
  else:
    cost = weight * 4.75
  return cost

#Ground Shipping
def ground_shipping(weight):
  cost = basic_shipping(weight)
  return cost + GS_FLAT
print("Ground Shipping:", ground_shipping(weight))

#Ground Shipping Premium
print("Ground Shipping Premium:", GSP_FLAT)

#Drone Shipping
def drone_shipping(weight):
  cost = basic_shipping(weight)
  return cost * 3
print("Drone Shipping:", drone_shipping(weight))
