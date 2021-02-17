# Sonny Li
# Fun Fact: I played guitar in a band called Attica.

print("  SSS   L     ")
print(" S   S  L     ")
print(" S      L     ")
print("  SSS   L     ")
print("     S  L     ")
print(" S   S  L     ")
print("  SSS   LLLLL ")

# You also can do it like this:

array1 = ["F ", "F ", "F ", "F ", "F "]
array2 = ["F ", "F ", "F ", "  ", "  "]
array3 = ["F ", "  ", "  ", "  ", "  "]

matrix = [array1, array3, array3, array2, array3, array3, array3]

for i in range(len(matrix)):
  linha_print = ""
  for w in range(len(matrix[i])):
    linha_print += matrix[i][w]
  print(linha_print)
