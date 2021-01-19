# Space Boxer 🥊
# Sonny Li

print("I have information for the following planets:\n")

print("   1. Venus   2. Mars    3. Jupiter")
print("   4. Saturn  5. Uranus  6. Neptune\n")
 
weight = 185
planet = 3

# Write an if statement below:

if planet == 1:
  weight = weight * 0.78
elif planet == 2:
  weight = weight * 0.39
elif planet == 3:
  weight = weight * 2.65
elif planet == 4:
  weight = weight * 1.17
elif planet == 5:
  weight = weight * 1.05
elif planet == 6:
  weight = weight * 1.23

print("Your weight:", weight)
