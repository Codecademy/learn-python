letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def unique_english_letters(word):
    counter = 0
    for letter in letters:
        if letter in word:
            counter += 1
    return counter


print(unique_english_letters("mississippi"))
print(unique_english_letters("Apple"))
print(unique_english_letters("Google"))

txt = "She said \"Never let go\"."
print(txt)
