def exponents(bases, powers):
    new_lst = []
    for base in bases:
        for power in powers:
            new_lst.append(base ** power)
    return new_lst


print(exponents([2, 3, 4], [1, 2, 3]))
