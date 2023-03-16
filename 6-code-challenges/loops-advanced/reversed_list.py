def reversed_list(lst1, lst2):
    for index in range(len(lst1)):
        if (lst1[index] != lst2[len(lst2) - (index + 1)]):
            return False

    return True

print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))
