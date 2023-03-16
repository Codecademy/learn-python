# def substring_between_letters(word, start, end):
#     if (word.find(start) == -1 or word.find(end) == -1):
#         return word
#     else:
#         substring = ""
#         for i in range(0, len(word)):
#             if i > word.find(start) and i < word.find(end):
#                 substring += word[i]
#         return substring


def substring_between_letters(word, start, end):
    start_ind = word.find(start)
    end_ind = word.find(end)
    if start_ind > -1 and end_ind > -1:
        return (word[start_ind+1:end_ind])
    return word


print(substring_between_letters("apple", "p", "e"))
print(substring_between_letters("apple", "p", "c"))
