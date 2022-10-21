weight = 4.8
cost = 0
cost_ground_premium = 125
cost_drone = 0

# Ground shipping costs
if weight <= 2.0:
    cost += float(weight) * 1.50 + 20
elif 2.0 < weight <= 6:
    cost += float(weight) * 3.00 + 20
elif 6.0 < weight <= 10:
    cost += float(weight) * 4.00 + 20
elif weight > 10:
    cost += float(weight) * 4.75 + 20
print("The regular shipping ground cost is: " + str(cost) + "$")

# Ground premium costs
print("The premium shipping ground cost is: " + str(cost_ground_premium) + "$")

# Drone shipping
if weight <= 2.0:
    cost_drone += float(weight) * 4.50
elif 2.0 < weight <= 6:
    cost_drone += float(weight) * 9.00
elif 6.0 < weight <= 10:
    cost_drone += float(weight) * 12.00
elif weight > 10:
    cost_drone += float(weight) * 14.25
print("The drone shipping cost is: " + str(cost_drone) + "$")
