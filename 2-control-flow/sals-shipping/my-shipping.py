#@Pietmkn (Piet Mokoena)
weight = 50
#Ground shipping
if weight <=2 :
  ground_shipping_cost = weight * 1.5 + 20
elif weight > 2 and weight <= 6:
  ground_shipping_cost = weight * 3.00 + 20
elif weight > 6 and weight <=10:
  ground_shipping_cost = weight * 4.00 + 20
else:
  ground_shipping_cost = weight * 4.75 + 20
print("Ground Shipping Cost $", ground_shipping_cost)

premium_ground_shipping_cost = 125.00
print("Premium Ground Shipping Cost $", premium_ground_shipping_cost)

if weight <= 2:
  drone_shipping_cost = weight * 1.5 * 3
elif weight > 2 and weight <=6:
  drone_shipping_cost = weight * 3.00 * 3
elif weight > 6 and weight <= 10:
  drone_shipping_cost = weight * 4.00 * 3
else:
  drone_shipping_cost = weight * 4.75 * 3
print("Drone Shipping Cost $",drone_shipping_cost)

# Determine the cheapest method
if ground_shipping_cost < premium_ground_shipping_cost and ground_shipping_cost < drone_shipping_cost:
    print("Cheapest method: Ground Shipping $", ground_shipping_cost)
elif premium_ground_shipping_cost < ground_shipping_cost and premium_ground_shipping_cost < drone_shipping_cost:
    print("Cheapest method: Premium Ground Shipping $", premium_ground_shipping_cost)
else:
     print("Cheapest method: Drone Shipping $", drone_shipping_cost)
