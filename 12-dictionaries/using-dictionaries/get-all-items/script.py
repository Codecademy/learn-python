pct_women_in_occupation = {
    "CEO": 28,
    "Engineering Manager": 9,
    "Pharmacist": 58,
    "Physician": 40,
    "Lawyer": 37,
    "Aerospace Engineer": 9
}

for key, value in pct_women_in_occupation.items():
    print("Women make up {value} percent of {key}s.".format(key=key, value=value))
