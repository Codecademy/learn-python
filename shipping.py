weight = 41.5

# Premium Shipping
premium_charge = 125.00

# Ground Shipping
if weight <= 2:
  ground_shipping_cost = weight * 1.5 + 20
elif weight > 2 and weight <= 6:
  ground_shipping_cost = weight * 3 + 20
elif weight > 6 and weight <= 10:
  ground_shipping_cost = weight * 4 + 20
else:
  ground_shipping_cost = weight * 4.75 + 20
rounded_shipping_cost = round(ground_shipping_cost, 2)  
print ("Ground Shipping: $" + str(rounded_shipping_cost))
print ("Premium Shipping: $" + str(premium_charge))

# Drone Shipping
if weight <= 2:
  drone_shipping_cost = weight * 4.5
elif weight > 2 and weight <= 6:
  drone_shipping_cost = weight * 9
elif weight > 6 and weight <= 10:
  drone_shipping_cost = weight * 12
else:
  drone_shipping_cost = weight * 14.25
rounded_shipping_cost = round(drone_shipping_cost, 2)  
print("Drone Shipping: $" + str(rounded_shipping_cost)) 

# How can I tell the program to say what the lowest method is? Code that would calculate the total of all 3, compare them, and print the lowest shipping cost?
# How do I make input commands that first ask what weight the package is and desired shipping method?
