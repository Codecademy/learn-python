# def reverse_string(word):
#     results = ""
#     for index in range(0, len(word)):
#         results += word[(len(word) - 1) - index]
#     return results


def reverse_string(word):
    reverse = ""
    for i in range(len(word)-1, -1, -1):
        reverse += word[i]
    return reverse


print(reverse_string("Codecademy"))
print(reverse_string("Hello world!"))
print(reverse_string(""))
