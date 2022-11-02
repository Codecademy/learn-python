def append_sum(lst):
    lst.append(lst[-1] + lst[-2])
    lst.append(lst[-1] + lst[-2])
    lst.append(lst[-1] + lst[-2])
    return lst


print(append_sum([1, 1, 2]))
