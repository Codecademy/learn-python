def over_budget(budget, food_bill, electricity_bill, internet_bill, rent):
    if budget < food_bill + electricity_bill + internet_bill + rent:
        return True
    else:
        return False


print(over_budget(100, 20, 30, 10, 40))
print(over_budget(80, 20, 30, 10, 30))
