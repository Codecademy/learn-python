def lots_of_math(a, b, c, d):
    first = a + b
    second = c - d
    third = first * second
    fourth = third % a

    print(first)
    print(second)
    print(third)
    return fourth


print(lots_of_math(1, 2, 3, 4))
print(lots_of_math(1, 1, 1, 1))
