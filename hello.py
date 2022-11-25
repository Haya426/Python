has_good_income = True
has_good_credit = False
has_criminal_records = False

if has_good_income and has_good_credit:
    print("Eligible payments")
elif has_good_credit or not has_good_credit:
    print("Eligible payments again")
