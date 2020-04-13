import math
from datetime import date, timedelta


def calculate_age_days():
    birthday = input()
    birthmonth = input()
    birthyear = input()
    born = date(int(birthyear), int(birthmonth), int(birthday))
    today = date.today()
    # return today.year - dog_born.year - ((today.month, today.day) < (dog_born.month, dog_born.day))
    age = today - born
    return age.days


def dog_to_human(dog_age):
    # ln(x) = log(x, e)
    # human_age = (16 * (math.log(int(dog_age), math.e))) + 31
    # y = -0.0289x2 + 5.1455x + 11.902 another dog equation made in excel from plotting medium dog conversion
    # y = -2E-11x4 + 3E-07x3 - 0.0013x2 + 7.2079x + 3404.8 same formula but in days
    # human_age = (-0.0289 * float(dog_age) ** 2) + (5.1455 * float(dog_age)) + 11.902
    human_age = ((-2 * (10 ** -11)) * (float(dog_age) ** 4)) + ((3 * (10 ** -7)) * (float(dog_age) ** 3)) - (0.0013 * (float(dog_age) ** 2)) + (7.2079 * float(dog_age)) + 3404.8
    return human_age


#print(dog_to_human())
#print(dog_date_to_years())
dog_age = calculate_age_days()
print(dog_age)
dog_human_age = dog_to_human(dog_age)
print(dog_human_age)

