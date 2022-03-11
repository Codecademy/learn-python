

weight = input("weight of item: ")

## Ground shipping 
fc = (20)
premium_ground_shipping = 125
print("premium ground shipping cost: " + str(premium_ground_shipping))
cost = 0
ppp = [1.5, 3.0, 4.0, 4.75]
if weight <= 2:
  cost = (fc + ppp[0]*weight)
elif 6 >= weight > 2:
  cost = (fc + ppp[1]*weight)
elif 10 >= weight > 6:
  cost = (fc + ppp[2]*weight)
else:
  cost = (fc + ppp[3]*weight)
print("Cost of deliervy is: " + str(cost))


## Drone shipping

cost_drone = 0
ppp_drone = [4.5, 9.0, 12.0, 14.25]
if weight <= 2:
  cost_drone = (ppp_drone[0]*weight)
elif 6 >= weight > 2:
  cost_drone = (ppp_drone[1]*weight)
elif 10 >= weight > 6:
  cost_drone = (ppp_drone[2]*weight)
else:
  cost_drone = (ppp_drone[3]*weight)
print("Cost of deliervy for drone is: " + str(cost_drone))
