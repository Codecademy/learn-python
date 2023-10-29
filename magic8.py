import random

name = "Gian"
question = "Is it going to rain today?"
answer = ""
random_number = random.randint(1, 10)

# print(random_number)

if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidely so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
elif random_number == 10:
  answer = "Maybe"
else:
  answer = "Error"


# This statement checks if question is empty
if question == "":
  print("No question, no fortune")
else:
  # This statement checks if name is empty
  if name == "":
    print(f"Question: {question}")
  else:
    print(f"{name} asks: {question}")

  print(f"Magic 8-Ball's answer: {answer}")
