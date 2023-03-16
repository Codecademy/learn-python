def count_multi_char_x(word, x):
    result = word.split(x)
    return len(result) - 1

print(count_multi_char_x("mississippi", "iss"))
print(count_multi_char_x("apple", "pp"))
