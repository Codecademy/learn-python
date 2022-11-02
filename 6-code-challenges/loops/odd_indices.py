def odd_indices(lst):
    new_lst = []
    for item in lst:
        if (lst.index(item) % 2 == 1):
            new_lst.append(item)
    return new_lst


print(odd_indices([4, 3, 7, 10, 11, -2]))
