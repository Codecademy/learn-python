weight = 50
#Weight of the package
#XXXXXXXXX#


#Ground shipping cost
print("GROUND SHIPPING COST")
if weight <= 2:
  print("The package will cost U$" + str(int(1.50 * weight + 20.00)) + " in ground shipping plan!")
  ground_shipping_cost = 1.50 * weight + 20.00
elif weight > 2 and weight <= 6:
  print("The package will cost U$" + str(int(3.00 * weight + 20.00)) + " in ground shipping plan!") 
  ground_shipping_cost = 3.00 * weight + 20.00
elif weight > 6 and weight <= 10:
  print("The package will cost U$" + str(int(4.00 * weight + 20.00)) + " in ground shipping plan!")
  ground_shipping_cost = 4.00 * weight + 20.00
elif weight > 10:
  print("The package will cost U$" + str(int(4.75 * weight + 20.00)) + " in ground shipping plan!")
  ground_shipping_cost = 4.75 * weight + 20.00
#XXXXXXXXXXXXXXX#

#Ground shipping premium cost
print("\n")
print("GROUND SHIPPING PREMIUM")
print("In ground shipping premium plan, the package will cost U$125!")
ground_shipping_premium_cost = 125
#XXXXXXXXXXXXXXXX#

#Drone shipping cost
print("\n")
print("DRONE SHIPPING")
if weight <= 2:
  print("The package will cost U$" + str(int(3 * 1.50 * weight)) + " in drone shipping plan!")
  drone_shipping_cost = 3 * 1.50 * weight
elif weight > 2 and weight <= 6:
  print("The package will cost U$" + str(int(3 * 3.00 * weight)) + " in drone shipping plan!")
  drone_shipping_cost = 3 * 3.00 * weight
elif weight > 6 and weight <= 10:
  print("The package will cost U$" + str(int(3 * 4.00 * weight)) + " in drone shipping plan!")
  drone_shipping_cost = 3 * 4.00 * weight
elif weight > 10:
  print("The package will cost U$" + str(int(3 * 4.75 * weight)) + " in drone shipping plan!") 
  drone_shipping_cost = 3 * 4.75 * weight
#XXXXXXXXXXXXXX#

#This will print the best shipping option for the customer
if ground_shipping_cost < drone_shipping_cost and ground_shipping_cost < ground_shipping_premium_cost:
  print("\n\n\n\n\nThe best cost-effectiveness of the shipping is the ground shipping plan! In this plan, you'll have a better choice for who searches for better prices and have a lighter package, but, due a high demand, the delivery service isn't so fast.")
elif drone_shipping_cost < ground_shipping_cost and drone_shipping_cost < ground_shipping_premium_cost:
  print("\nThe best cost-effectiveness of the shipping is the drone shipping plan! Get a fast delivery, and a total package insurance! Your package will be totally protected and we can affort that the freight will be arrive in less then 3 days! (Don't worry, no freak'in box is going to fall above your head out of nowhere.)")
elif ground_shipping_premium_cost < ground_shipping_cost and ground_shipping_premium_cost < drone_shipping_cost:
  print("\n\n\n\n\nThe best cost-effectiveness of the shipping is the ground shipping premium plan! Due a heavy weight of your package, we can affort that the ground shipping premium plan, it's your chance to acquire a good service, both for a fast delivery, and for package insurance!")
