import math
from datetime import date, timedelta


def calculate_age_days():
    """Takes user input for day, month, and year and returns the users age in days"""
    birthday = input()
    birthmonth = input()
    birthyear = input()
    born = date(int(birthyear), int(birthmonth), int(birthday))
    today = date.today()
    age = today - born
    return age.days


def dog_to_human(dog_age):
    """Takes dogs age in days as input and converts it into the equivalent human age in days"""
    # ln(x) = log(x, e)
    # human_age = (16 * (math.log(int(dog_age), math.e))) + 31 known best dog age formula
    # y = 8E-15x6 - 6E-11x5 + 1E-07x4 - 0.0002x3 + 0.0764x2 + 2.3013x - 16.923 equation for 0 - 6 years old
    # y = 4.5x + 5566.3 equation for 6 - 30 years old
    if dog_age < 0:
        print("Dog age must be greater than 0")
        return -1
    elif dog_age > 0 and dog_age < 2191.455:
        human_age = ((8 * (10 ** -15)) * (float(dog_age) ** 6)) - ((6 * (10 ** -11)) * (float(dog_age) ** 5)) + ((1 * (10 ** -7)) * (float(dog_age) ** 4)) - (0.0002 * (float(dog_age) ** 3)) + (0.0764 * (float(dog_age) ** 2)) + (2.3013 * (float(dog_age))) - 16
        return human_age
    elif dog_age >= 2191.455 and dog_age < 10957.275:
        human_age = (4.5 * float(dog_age)) + 5566.3
        return human_age
    else:
        print("Dog age must be less than 30 years old")
        return -1

#print(dog_to_human())
#print(dog_date_to_years())
dog_age = calculate_age_days()
print(dog_age)
dog_human_age = dog_to_human(dog_age)
print(dog_human_age)

