weight = 41.5
#ground shipping
if(weight<2):
  g_price = weight * 1.50 + 20.00
  print("Ground shipping price is : " + str(g_price))
elif(weight>2 and weight <= 6):
  g_price = weight * 3.00 + 20.00
  print("Ground shipping price is : " + str(g_price))
elif(weight>6 and weight <= 10):
  g_price = weight * 4.00 + 20.00
  print("Ground shipping price is : " + str(g_price))
elif(weight>10):
  g_price = weight * 4.75 + 20.00
  print("Ground shipping price is :" + str(g_price))

#drone shipping

if(weight<2):
  d_price = weight * 4.50
  print("Drone shipping price is : " + 
   str(d_price))
elif(weight>2 and weight <= 6):
  d_price = weight * 9.00
  print("Drone shipping price is : " + str(d_price))
elif(weight>6 and weight <= 10):
  d_price = weight * 12.00
  print("Drone shipping price is : " + str(d_price))
elif(weight>10):
  d_price = weight * 14.25
  print("Drone shipping price is : " + str(d_price))

if(g_price < d_price):
  print("Ground shipping is cheaper and thus we reccomend you to use this package")
elif(g_price > d_price):
    print("Drone shipping is cheaper and thus we reccomend you to use this package")
else:
  print("Both are of same price, so you are more than welcomed to choose the package you prefer.")
