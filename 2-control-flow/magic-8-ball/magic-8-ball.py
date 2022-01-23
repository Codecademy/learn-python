import random

playerName = "Galina"
playerQuestion = "Will there be any more snowfall in New York for winter 2020? ❄️"

randomNumber = random.randint(1, 9)
# randomNumber = "xyz"
# print(randomNumber)

switcher = {
    1: "Yes - definitely",
    2: "It is decidedly so",
    3: "Without a doubt",
    4: "Reply hazy, try again",
    5: "Ask again later",
    6: "Better not tell you now",
    7: "My sources say no",
    8: "Outlook not so good",
    9: "Very doubtful",
}

print(playerName, "\'s Question:", playerQuestion)

# Challenge:
# playerName.isEmpty ? print("Question: \(playerQuestion)") : print("\(playerName) asks: \(playerQuestion)")

print(switcher.get(randomNumber, "Error"))
