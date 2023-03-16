def count_char_x(word, x):
    occurrences = 0
    for letter in word:
        if letter == x:
            occurrences += 1
    return occurrences


print(count_char_x("mississippi", "s"))
print(count_char_x("mississippi", "m"))
