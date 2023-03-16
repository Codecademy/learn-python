letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
letter_to_points = {key: value for key, value in zip(letters, points)}
letter_to_points[" "] = 0

player_to_words = {
    "player1": ["BLUE", "TENNIS", "EXIT"],
    "wordNerd": ["EARTH", "EYES", "MACHINE"],
    "Lexi Con": ["ERASER", "BELLY", "HUKSY"],
    "Prof Reader": ["ZAP", "COMA", "PERIOD"]
}
player_to_points = {}


def score_word(word):
    point_total = 0
    for letter in word.upper():
        point_total += letter_to_points.get(letter, 0)
    return point_total


def play_word(player, word):
    try:
        player_to_words[player].append(word)
    except KeyError:
        print("That key doesn't exist!")


def update_point_totals():
    for player, words in player_to_words.items():
        player_points = 0
        for word in words:
            player_points += score_word(word)
        player_to_points[player] = player_points


brownie_points = score_word("brownie")
print(brownie_points)

update_point_totals()
print(player_to_points)

play_word("player1", "LOVE")
update_point_totals()
print(player_to_points)
