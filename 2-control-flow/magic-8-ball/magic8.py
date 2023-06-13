name = "Jessica"

question = "¿Ganaré la lotería?"

answer = ""

import random

random_number = random.randint(1, 9)

print(random_number)

if random_number == 1:
  answer = "Al chile si"
elif random_number == 2:
  answer = "Es decididamente así"
elif random_number == 3:
  answer = "Sin duda"
elif random_number == 4:
  answer = "Respuesta confusa, intenta otra vez"
elif random_number == 5:
  answer = "No me molestes xd"
elif random_number == 6:
  answer = "Mejor mañana, diantre xd"
elif random_number == 7:
  answer = "Mis fuentes dicen que no"
elif random_number == 8:
  answer = "Al chile no"
elif random_number == 9:
  answer = "No sepo, diablo jeje"
else:
  answer = "Error"


print(name + " pregunta: " + question)


print("Bola mágica responde: " + answer)
