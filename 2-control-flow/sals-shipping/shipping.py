weight = 41.5
ground_shipping = 0.0
ground_premium = 125
drone_shipping = 0.0


#Ground Shipping
if weight <= 2 and weight > 0:
  ground_shipping = weight * 1.5 + 20
elif weight <= 6 and weight > 2:
  ground_shipping = weight * 3 + 20
elif weight <= 10 and weight > 6:
  ground_shipping = weight * 4 + 20
else:
  ground_shipping = weight * 4.75 + 20

#drone shipping
if weight <= 2 and weight > 0:
  drone_shipping = weight * 4.5
elif weight <=6 and weight > 2:
  drone_shipping = weight * 9
elif weight <= 10 and weight > 6:
  drone_shipping = weight * 12
elif weight > 10:
  drone_shipping = weight * 14.25

#prints prices of all 3 types of shipping and makes sure weight is valid
if weight <= 0:
  print("Please input a valid package weight")
else:
  print("Ground shipping:", ground_shipping)
  print("Ground shipping premium:", ground_premium)
  print("Drone shipping:", drone_shipping)

#checks which price is lowest and informs the customer
if ground_shipping < ground_premium and ground_shipping < drone_shipping and ground_shipping > 0:
  print("Your best option for a package weighing", weight, "pounds is ground shipping")
elif ground_premium < ground_shipping and ground_premium < drone_shipping and ground_premium > 0:
  print("Your best option for a package weighing", weight, "pounds is ground shipping premium")
elif drone_shipping < ground_shipping and drone_shipping < ground_premium and drone_shipping > 0:
  print("Your best option for a package weighing", weight, "pounds is drone shipping")
