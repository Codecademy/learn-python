# Sal's Shipping
# Loctogan

weight = 80
weight=int(input("Combien pèse votre colis?"))
# Livraison par route 🚚
flat_charge = 20
if weight <= 2:
  cost_ground = weight * 1.5 + flat_charge
elif weight <= 6:
  cost_ground = weight * 3.00 + flat_charge
elif weight <= 10:
  cost_ground = weight * 4.00 + flat_charge
else:
  cost_ground = weight * 4.75 + flat_charge

print("Ground Shipping $", cost_ground)

# Livraison premium 🚚

cost_premium_shipping = 125
print("Premium Shipping $", cost_premium_shipping)
# drone Shipping 🚁

if weight <= 2:
  cost_drone = weight * 4.5
elif weight <= 6:
  cost_drone = weight * 9
elif weight <= 10:
  cost_drone = weight * 12
else:
  cost_drone = weight * 14.25

print("Drone Shipping $", cost_drone)

meilleure_offre = 0
type_livraison= "aucune"
if cost_ground<cost_drone and cost_drone<cost_premium_shipping:
  meilleure_offre=cost_ground
  type_livraison="standard"
elif cost_drone<cost_ground and cost_drone<cost_premium_shipping:
  meilleure_offre=cost_drone
  type_livraison="par drone"
else:
  meilleure_offre=cost_premium_shipping
  type_livraison="premium"

print ("La meilleur offre est la livraison ",type_livraison,"et coûte",meilleure_offre,".- chfs")
