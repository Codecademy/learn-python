def x_length_words(sentence, x):
    for word in sentence.split():
        if len(word) < x:
            return False
    return True


print(x_length_words("i like apples", 2))
print(x_length_words("he likes apples", 2))
