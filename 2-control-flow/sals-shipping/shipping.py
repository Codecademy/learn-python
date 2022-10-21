#Written for python 3.9
#Created by tankmaster077 @ 5/15/21

"""This script calculates the cost of each shipping method and returns the cheapest option based on weight"""

weight = 2
ground_flat = 20.00
prem_ground = 125.00

#Ground Shipping
def ground_shipping(weight):
    if weight <= 2:
      cost = (weight*1.50) + ground_flat
    elif weight > 2 and weight<= 6:
      cost = (weight*3.00) + ground_flat
    elif weight > 6 and weight <= 10:
      cost = (weight*4.00) + ground_flat
    else:
      cost = (weight*4.75) + ground_flat
    return cost
  
#Drone Shipping
def drone_shipping(weight):
    if weight <= 2:
      cost = (weight*4.50)
    elif weight > 2 and weight<= 6:
      cost = (weight*9.00)
    elif weight > 6 and weight <= 10:
      cost = (weight*12.00)
    else:
      cost = (weight*14.25) 
    return cost

cheapest_cost = [ground_shipping(weight), prem_ground, drone_shipping(weight)]
  
print (f"Ground Shipping Cost: ${ground_shipping(weight)}")
print (f"Premium Ground Cost: ${prem_ground}")
print (f"Drone Shipping Cost: ${drone_shipping(weight)}")
print (f"Cheapest Cost to Ship: ${min(cheapest_cost)}")
