weight = int(input("Weight: "))
unit = input("(L)lbs or (K) kg: ")
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} kg")
else:
    converted = weight / 0.45
    print(f"You are {converted} pounds")