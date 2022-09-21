weight = int(input("What is your package weight? "))

# Ground Shipping cost
gs_cost = 0
fc_gs = 20

if weight <= 2:
    gs_cost = weight * 1.5 + fc_gs
elif weight <= 6:
    gs_cost = weight * 3 + fc_gs
elif weight <= 10:
    gs_cost = weight * 4 + fc_gs
else:
    gs_cost = weight * 4.75 + fc_gs

# Ground shipping premium cost
gsp_cost = 125

# Drone shipping cost
ds_cost = 0
if weight <= 2:
    ds_cost = weight * 4.5
elif weight <= 6:
    ds_cost = weight * 9
elif weight <= 10:
    ds_cost = weight * 12
else:
    gs_cost = weight * 14.25

print("The cost for 3 shipping methods is:")
print("Ground Shipping cost is        : ", gs_cost, "$")
print("Ground Shipping Premium cost is: ", gsp_cost, "$")
print("Drone Shipping cost is         : ", ds_cost, "$")

if (gs_cost<gsp_cost) and (gs_cost<ds_cost):
    print("Ground Shipping is your best option with amount: ", gs_cost)
if (gsp_cost < gs_cost) and (gsp_cost < ds_cost):
    print("Ground Shipping Premium is your best option with amount: ", gsp_cost)
if (ds_cost < gs_cost) and (ds_cost < gsp_cost):
    print("Drone Shipping is your best option with amount: ", ds_cost, "$")
