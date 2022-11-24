birth_year = input('enter your birth year')
print(type(birth_year))
age = 2022 - int(birth_year) # type conversion from string to number
print(type(age))
print(age)

weight_lbs = input('Weight in lbs: ')
weight_kg = float(weight_lbs) * 0.45
print(weight_kg)


