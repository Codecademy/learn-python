#Sal's Shipping
#Alyssa H.


#Some Weight
weight = 41.5

#Ground Shipping (gcost)
flat_charge = 20.00

if weight <= 2.00:
  gcost = flat_charge + (1.50 * weight)
elif weight > 2.00 and weight <= 6.00:  
  gcost = flat_charge + (3.00 * weight)
elif weight > 6.00 and weight <= 10.00:
  gcost = flat_charge + (4.00 * weight) 
else:
  gcost = flat_charge + (4.75 * weight)

#premium cost (pcost)
pcost = 125.00


#drone shipping (dcost)
if weight <= 2.00:
  dcost = (weight * 4.50)
elif weight > 2.00 and weight <= 6.00:
  dcost = (weight * 9.00)
elif weight > 6.00 and weight <= 10.00:
  dcost = (weight * 12.00)
else:
  dcost = (weight * 14.25)

# cheapest cost 
if dcost < gcost and dcost < pcost:
  cheapest_cost = dcost
  sm = "Drone Shipping"
elif gcost < dcost and gcost < pcost:
  cheapest_cost = gcost
  sm = "Ground Shipping"
else:
  cheapest_cost = pcost
  sm = "Premium Ground Shipping"
  
print("The cheapest shipping option for a package with the weight of " + str(weight) + "lbs. is $" + str(cheapest_cost) + " through " + sm)
   