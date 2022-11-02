def remove_middle(lst, start, end):
    before_start_index = lst[:start]
    after_end_index = lst[end+1:]
    return before_start_index + after_end_index


print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))
