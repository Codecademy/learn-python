def same_values(lst1, lst2):
    list_indices = []

    for index in range(len(lst1)):
        if (lst1[index] == lst2[index]):
            list_indices.append(index)

    return list_indices


print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))
