def middle_element(lst):
    if len(lst) % 2 == 0:
        sum = lst[int(len(lst) / 2)] + lst[int(len(lst) / 2) - 1]
        return sum / 2
    else:
        return lst[int(len(lst) / 2)]


print(middle_element([5, 2, -10, -4, 4]))
