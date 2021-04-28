#Prolonpo's Version
#Able to directly see the cheapest shipping option without having to sort through and decide which one is cheaper manually

#Weight of package in pounds
weight = 0.5

#Shipping price (start at 0)
price = 0

#Ground Shipping

if weight <= 2:
  price = 20 + 1.50 * weight
elif weight <= 6:
  price = 20 + 3.00 * weight
elif weight <= 10:
  price = 20 + 4.00 * weight
else:
  price = 20 + 4.75 * weight

#print("Ground Shipping would cost: $", price)

#Premium Ground Shipping

price_premium = 125
#Flat rate, doesn't change

#print("Premium Ground shipping would cost: $",price_premium)

#Drone shipping

price_drone = 0
#No shipping fee to start with

if weight <= 2:
  price_drone = 4.50 * weight
elif weight <= 6:
  price_drone = 9.00 * weight
elif weight <= 10:
  price_drone = 12.00 * weight
else:
  price_drone = 14.25 * weight

#print("Drone Shipping would cost: $", price_drone)

#Answering Q from step 8
#Cheapest method for 4.8 pounds: ground shipping, cost $34.40
#Cheapest method for 41.5 pounds: premium ground shipping, cost $125

#Personal note: how would I be able to write a sentence stating which option is the cheapest?
#Great question me, let's try this:

#Printing out cheapest option and its price - note, created a variable "price_drone"

print("With a weight of", weight, "lbs")

if price <= price_premium and price <= price_drone:
  print("\nCheapest option is: Ground Shipping, which will cost $", price)
elif price_premium <= price and price_premium <= price_drone:
  print("\nCheapest option is: Premium Ground Shipping, which will cost $", price_premium)
elif price_drone <= price and price_drone <= price_premium:
  print("\nCheapest option is: Drone Shipping, which will cost $", price_drone)

#Note, if comment out the previous print() statement for cost of Ground Shipping, Premium Ground Shipping, and Drone Shipping, end up with only the cheapest option based on the entered value
