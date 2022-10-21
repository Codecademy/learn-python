#Sal's Shipping exercise
#Added input from user for weight and responses specific to the most cost-efficient method.

#get weight from user
weight_str = input('What is the weight in pounds?')

#convert str to int from input
weight_float = float(weight_str)

#ground shipping control flow
if weight_float <= 2:
    price_per_pound_ground = 1.50
elif weight_float > 2 and weight_float <= 6:
    price_per_pound_ground = 3.00
elif weight_float > 6 and weight_float <= 10:
    price_per_pound_ground = 4.00
else:
    price_per_pound_ground = 4.75

#drone shipping control flow
if weight_float <= 2:
    price_per_pound_drone = 4.5
elif weight_float > 2 and weight_float <= 6:
    price_per_pound_drone = 9.00
elif weight_float > 6 and weight_float <= 10:
    price_per_pound_drone = 12.00
else:
    price_per_pound_drone = 14.25

#define cost for each method
groundcost = weight_float * price_per_pound_ground + 20.00
dronecost = weight_float * price_per_pound_drone 

#define premium amount
premium_ground = 125

#print the most cost-effective method with price included
if groundcost < dronecost:
    print('The most cost-efficient method to ship this is via ground and will cost: $' + str(groundcost))
elif dronecost < groundcost:
    print('The most cost-efficient method to ship this is via drone and will cost: $' + str(dronecost))
elif dronecost == groundcost and dronecost < premium_ground and groundcost < premium_ground:
    print("It will cost the same to ship this package via drone or ground. The cost is: $" + str(dronecost))
else: 
    print("The most cost-efficient method to ship this will be via Premium Ground and cost: $" + str(premium_ground))
