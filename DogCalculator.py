from datetime import date, timedelta
from numpy import roots, polyval

def date_input():
    birthday = input()
    birthmonth = input()
    birthyear = input()
    born = date(int(birthyear), int(birthmonth), int(birthday))
    return born

def calculate_age_days(year, month, day):
    """Takes user input for day, month, and year and returns the users age in days"""
    today = date.today()
    age = today - date(int(year), int(month), int(day))
    return age.days


def dog_to_human(dog_age):
    """Takes dogs age in days as input and converts it into the equivalent human age in days"""
    # todo 0 to 6 function isn't working properly need a better one
    # ln(x) = log(x, e)
    # human_age = (16 * (math.log(int(dog_age), math.e))) + 31 known best dog age formula
    # y = 0.0441x2 + 2.5382x equation for 0 - 1 years old
    # y = -0.0068x2 + 16.868x equation for 1 - 4 years old
    # y = -0.0018x2 + 10.857x equation for 3 - 6 years old
    # y = -0.0001x2 + 6.2952x equation for 6 - 30 years old (picked 30 years since oldest dog ever is 29)
    if dog_age < 0:
        print("Dog age must be greater than 0")
        return -1
    elif 0 <= dog_age < 243.5:
        human_age = (0.0441 * (float(dog_age) ** 2)) + (2.5382 * float(dog_age))
        # returning 1 since it is in the first age grouping
        return human_age
    elif 243.5 <= dog_age < 1095.7275:
        human_age = (-0.0068 * (float(dog_age) ** 2)) + (16.868 * float(dog_age))
        return human_age
    elif 1095.7275 <= dog_age < 2191.455:
        human_age = (-0.0018 * (float(dog_age) ** 2)) + (10.857 * float(dog_age))
        return human_age
    elif 2191.455 <= dog_age < 10957.275:
        human_age = (-0.0001 * (float(dog_age) ** 2)) + (6.2952 * float(dog_age))
        return human_age
    else:
        print("Dog age must be less than 30 years old")
        return -1

def x_vertex(a, b):
    xcoord = - b / (2 * a)
    return xcoord


def dog_human_intersect(human_age, dog_human_age):
    # todo make a check to make sure humans age is greater than the dogs
    # todo for age less than 1 the parabola is going upwards so the root cannot be greater than 0 and be less than the vert
    # dog_in_human_age + dog_to_human(x) = human_age + x
    # x is the number of human years it will take for both dog and human to be the same age
    # polynomial ax^2 + bx + c
    # y = -0.0001x2 + 6.4551x
    a = -0.0001
    b = 6.4551
    c = human_age - dog_human_age
    # our equation has ax^2 + bx = c so we need to do -c
    xroots = roots([a, b - 1, -c])
    # the only root we want is the x value before the peak of the parabola
    xvert = x_vertex(a, b)
    for root in xroots:
        if xvert > root > 0:
            return root
        else:
            continue
    return -1


def dog_human_date(intersect, human_age, dog_age):
    today = date.today()
    same_age_date = today + timedelta(days=intersect)
    dog_new_age = dog_age + intersect
    human_new_age = human_age + intersect
    human_new_age_years = human_new_age/365.2425
    dog_new_age_years = dog_new_age/365.2425
    print(human_new_age_years)
    print(dog_new_age_years)
    if round(dog_new_age_years) > dog_new_age_years:
        print("Your dog will almost be", round(dog_new_age_years), " years old")
    else:
        print("Your dog will be ", round(dog_new_age_years), " years old")
    if round(human_new_age_years) > human_new_age_years:
        print("You will be almost", round(human_new_age_years), " years old")
    else:
        print("You will be", round(human_new_age_years), " years old")
    return same_age_date

#print(dog_to_human())
#print(dog_date_to_years())
dog_age = calculate_age_days(2020, 3, 15)
print(dog_age)
dog_human_age = dog_to_human(dog_age)
print(dog_human_age)
# dog_human_age2 = dog_to_human(3805)
# print(dog_human_age2)
print("You are ", 16790/365.2425, " years old")
print("Your dog is  ", dog_age/365.2425, " years old")
intersect = dog_human_intersect(16790, dog_human_age)
print(intersect)
human_same_age = dog_human_date(intersect, 16790, dog_age)
print(human_same_age)