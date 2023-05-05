print("I have information for the following planets:\n")
print("   1. Venus   2. Mars    3. Jupiter")
print("   4. Saturn  5. Uranus  6. Neptune\n")
 
weight = 185
planet = 6

# Displays how much you weigh on the selected Planet rounded up to 2 decimal places.

if planet == 1:
  weight = weight * 0.94
  rounded_number = round(weight, 2)
  print ("On Venus, you weigh " + str(weight))
  print ("On Venus, you weigh " + str(rounded_number))
elif planet == 2:
  weight = weight * 0.38
  rounded_number = round(weight, 2)
  print ("On Mars, you weigh " + str(weight))
  print ("On Mars, you weigh " + str(rounded_number))
elif planet == 3:
  weight = weight * 2.34
  rounded_number = round(weight, 2)
  print ("On Jupiter, you weigh " + str(weight))
  print ("On Jupiter, you weigh " + str(rounded_number))
elif planet == 4:
  weight = weight * 1.06
  rounded_number = round(weight, 2)
  print ("On Saturn, you weigh " + str(weight))
  print ("On Saturn, you weigh " + str(rounded_number))
elif planet == 5:
  weight = weight * 0.92
  rounded_number = round(weight, 2)
  print ("On Uranus, you weigh " + str(weight))
  print ("On Uranus, you weigh " + str(rounded_number))
elif planet == 6:
  weight = weight * 1.19
  rounded_number = round(weight, 2)
  print ("On Neptune, you weigh " + str(weight))
  print ("On Neptune, you weigh " + str(rounded_number)) 
  
# To show rounded and rounded numbers.
