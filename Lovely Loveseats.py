# Lovely_loveseat is the name of the seat
lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high * 30 inches deep. Red or white."
# This is how much a chair will cost
lovely_loveseat_price = 254.00
# This is a description for a Stylish Settee
stylish_settee_description = "Stylish Settee. Faux leather on birch. 29.50 inches high * 54.75 inches wide * 28 inches deep. Black."
# This is how much it'll cost
stylish_settee_price = 180.50
# This is the description of a luxurious lamp
luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."

luxurious_lamp_price = 52.15

sales_tax = .088

customer_one_total = 0
customer_one_itemization = ""

customer_one_total += lovely_loveseat_price
customer_one_itemization += lovely_loveseat_description

customer_one_total += luxurious_lamp_price
customer_one_itemization += luxurious_lamp_description

customer_one_tax = customer_one_total * sales_tax
customer_one_total += customer_one_tax

print("Customer One Items:")
print(customer_one_itemization)
print("Customer One Total:")
print(customer_one_total)

customer_two_total = 0
customer_two_itemization = ""

customer_two_total += stylish_settee_price
customer_two_itemization += stylish_settee_description

customer_two_total += luxurious_lamp_price
customer_two_itemization += luxurious_lamp_description

customer_two_tax = customer_two_total * sales_tax
customer_two_total += customer_two_tax

print("Customer Two Items")
print(customer_two_itemization)
print("Customer Two Total:")
print(customer_two_total)
