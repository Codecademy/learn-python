def combine_sort(lst1, lst2):
    unsorted = lst1 + lst2
    sortedList = sorted(unsorted)
    return sortedList


print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))
