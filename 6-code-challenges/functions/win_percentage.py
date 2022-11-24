def win_percentage(wins, losses):
    total = wins + losses
    winning_ratio = wins / total * 100
    return int(winning_ratio)


print(win_percentage(5, 5))
print(win_percentage(10, 0))
