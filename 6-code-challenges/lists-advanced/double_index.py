def double_index(lst, index):
    if index >= len(lst):
        return lst
    else:
        # Gets the original list up to index
        sliced_lst = lst[0:index]
        # Adds double the value at index to the new list
        sliced_lst.append(lst[index] * 2)
        #  Adds the rest of the original list
        new_lst = sliced_lst + lst[index+1:]
        return new_lst


print(double_index([3, 8, -10, 12], 2))
