letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"


def unique_english_letters(word):
    counter = 0
    for letter in letters:
        if (letter in word):
            counter += 1
    return counter


print(unique_english_letters("miSsissippi"))
print(unique_english_letters("Apple"))
