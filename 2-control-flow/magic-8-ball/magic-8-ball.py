# Magic 8-Ball 🎱
# Galina Podstrechnaya

import random

playerName = "Galina"
playerQuestion = "Will there be any more snowfall in New York for winter 2020? ❄️" 

randomNumber = random.randint(1, 9)
# print(randomNumber)

if randomNumber == 1:
  eightBall = "Yes - definitely"
elif randomNumber == 2:
  eightBall = "It is decidedly so"
elif randomNumber == 3:
  eightBall = "Without a doubt"
elif randomNumber == 4:
  eightBall = "Reply hazy, try again"
elif randomNumber == 5:
  eightBall = "Ask again later"
elif randomNumber == 6:
  eightBall = "Better not tell you now"
elif randomNumber == 7:
  eightBall = "My sources say no"
elif randomNumber == 8:
  eightBall = "Outlook not so good"
elif randomNumber == 9:
  eightBall = "Very doubtful"
else:
  eightBall = "Error"

print(playerName, "\'s Question:", playerQuestion)

# Challenge:
#if question == "":
#    print("You forgot to ask a question!")
#else:
#    print(f"Question: {playerQuestion}" if name == "" else f"{playerName} asks: {playerQuestion}")
#    print("🎱:", playerName)

print("🎱:", eightBall)
