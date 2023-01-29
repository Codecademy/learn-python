# def every_other_letter(word):
#     results = ""
#     for index in range(len(word)):
#         if (index % 2 == 0):
#             results += word[index]
#     return results


def every_other_letter(word):
    every_other = ""
    for i in range(0, len(word), 2):
        every_other += word[i]
    return every_other


print(every_other_letter("Codecademy"))
print(every_other_letter("Hello world!"))
print(every_other_letter(""))
