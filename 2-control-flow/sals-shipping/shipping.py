# Sal's Shipping
# Dianicata
currency ="$"
import random

weight = random.randint(1, 150)
print("current random weight: " + str(weight))
# weight = 1.5

#Ground shipping
ground_shipping_flat_charge = 20

if weight <= 2 and weight >= 0:
  ground_shipment_cost = round(weight * 1.50 + ground_shipping_flat_charge, 2)
elif weight >= 2 and weight <= 6:
  ground_shipment_cost = round(weight * 3 + ground_shipping_flat_charge, 2)
elif weight >= 6 and weight <=10:
  ground_shipment_cost = round(weight * 4 + ground_shipping_flat_charge, 2)
elif weight > 10:
  ground_shipment_cost = round(weight * 4.75 + ground_shipping_flat_charge, 2)
else:
  ground_shipment_cost = "Error: Please tell me the right weight of your package"
print(f"Ground shipping option: {ground_shipment_cost}" + currency) 

# Ground_shipping_premium
premium_flat_charge = 125
print(f"Premium flat charge: {premium_flat_charge}" + currency)

# drone shipping
if weight <= 2 and weight >= 0:
  drone_shipment_cost = round(weight * 4.50, 2)
elif weight >= 2 and weight <= 6:
  drone_shipment_cost = round(weight * 9, 2) 
elif weight >= 6 and weight <= 10:
  drone_shipment_cost = round(weight * 12, 2)
elif weight > 10:
 drone_shipment_cost = round(weight * 14.25, 2)
else:
  drone_shipment_cost = "Error: Please tell me the right weight of your package"
print(f"Drone shipping option: {drone_shipment_cost}" + currency) 

# Cheapest option

shipping_option = ""
shipping_cost = 0
if ground_shipment_cost < premium_flat_charge and ground_shipment_cost < drone_shipment_cost:
  shipping_option = "ground shipping"
  shipping_cost = ground_shipment_cost
elif premium_flat_charge < ground_shipment_cost and premium_flat_charge < drone_shipment_cost:
  shipping_option = "premium flat charge"
  shipping_cost = premium_flat_charge
elif drone_shipment_cost < premium_flat_charge and drone_shipment_cost < ground_shipment_cost:
  shipping_option = "drone shipping"
  shipping_cost = drone_shipment_cost

print(f"Cheapest shipment option is with {shipping_option}: {shipping_cost}" + currency)