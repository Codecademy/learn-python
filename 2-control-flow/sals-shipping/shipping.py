#Sal's Shipping

package_weight = 4.8;

# check ground
def check_ground(package_weight):
  ground = 0;

  ground += 20;
  if package_weight <= 2:
    ground += package_weight*1.5;
  elif package_weight > 2 and package_weight <= 6:
    ground += package_weight*3;
  elif package_weight > 6 and package_weight <= 10:
    ground += package_weight*4;
  else:
    ground += package_weight*4.75;
  return ground;

# check drone
def check_drone(package_weight):
  drone = 0;

  if package_weight <= 2:
    drone += package_weight*4.5;
  elif package_weight > 2 and package_weight <= 6:
    drone += package_weight*9;
  elif package_weight > 6 and package_weight <= 10:
    drone += package_weight*12;
  else:
    drone += package_weight*14.25;
  return drone;


def final_shipping(package_weight):
  ground = check_ground(package_weight);
  ground_premium = 125;
  drone = check_drone(package_weight);

  cheapest_option = "";
  cheapest_price = 0;
  
  if ground < ground_premium and ground < drone:
    cheapest_option = "Ground Shipping";
    cheapest_price += ground; 
  elif ground_premium < ground and ground_premium < drone:
    cheapest_option = "Ground Shipping Premium";
    cheapest_price += ground_premium;
  else:
    cheapest_option = "Drone Shipping";
    cheapest_price += drone;

  # Print final cheapest option
  print("Ground Shipping is: $" + format(ground, ".2f"));
  print("Ground Shipping Premium is: $" + format(ground_premium, ".2f"));
  print("Drone Shipping is: $" + format(drone, ".2f"));
  print("======================")
  print("The cheapest option is " + cheapest_option + ". The cost to ship your " + str(package_weight) + "lb package, will be $" + format(cheapest_price, ".2f") + ".");

final_shipping(package_weight);


    
