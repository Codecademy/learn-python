#Declare variables
weight = 41.5
cost = 0
gr_sh_cost = 0
gr_sh_pre_cost = 125.00
dr_sh_cost = 0

#Calculate the cost for Ground Shipping
if weight <= 2:
  gr_sh_cost += weight*1.5 + 20
elif weight > 2 and weight <= 6:
  gr_sh_cost += weight*3 + 20
elif weight > 6 and weight <= 10:
  gr_sh_cost += weight*4 + 20
else:
  gr_sh_cost += weight*4.75 + 20
#print("The cost for Ground Shipping: " + str(gr_sh_cost))
#Calculate the cost for Drone Shipping
if weight <= 2:
  dr_sh_cost += weight*4.5
elif weight > 2 and weight <= 6:
  dr_sh_cost += weight*9
elif weight > 6 and weight <= 10:
  dr_sh_cost += weight*12
else:
  dr_sh_cost += weight*14.25
#print("The cost for Drone Shipping " + str(dr_sh_cost))
#The cost for Ground Shipping Premium
#print("The cost for Ground Shipping Premium: " + str(gr_sh_pre_cost))

#Chose the cheapest method of shipping
if gr_sh_cost < gr_sh_pre_cost and gr_sh_cost < dr_sh_cost:
  print("The cheapest method of shipping is: Ground Shipping.")
  print("You will pay: " + str(gr_sh_cost))
else:
  if gr_sh_pre_cost < dr_sh_cost:
    print("The cheapest method of shipping is: Ground Shipping Premium.")
    print("You will pay: " + str(gr_sh_pre_cost))
  else:
    print("The cheapest method of shipping is: Drone Shipping.")
    print("You will pay: " + str(dr_sh_cost))
