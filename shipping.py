# Sal's Shipping

weight = 4.8

premium_price = 125

# Ground Shipping
if weight <= 2:
  print(f"Total ground shipping cost is £{(weight * 1.50) + 20}")
elif 2 < weight <= 6:
  print(f"Total ground shipping cost is £{(weight * 3.00) + 20}")
elif 6 < weight <= 10:
  print(f"Total ground shipping cost is £{(weight * 4.00) + 20}")
else:
  print(f"Total ground shipping cost is £{(weight * 4.75) + 20}")

print(f"\nGround shipping premium price is £{premium_price}\n")

# Drone Shipping
if weight <= 2:
  print(f"Total drone shipping cost is £{weight * 4.50}")
elif 2 < weight <= 6:
  print(f"Total drone shipping cost is £{weight * 9.00}")
elif 6 < weight <= 10:
  print(f"Total drone shipping cost is £{weight * 12.00}")
else:
  print(f"Total drone shipping cost is £{weight * 14.25}")
