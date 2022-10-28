def in_range(num, lower, upper):
    if (num >= lower and num <= upper):
        return True
    else:
        return False


print(in_range(10, 10, 10))
print(in_range(5, 10, 20))
