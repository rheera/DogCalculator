from datetime import date, timedelta
from numpy import roots, polyval

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
    # todo 0 to 6 function isn't working properly need a better one
    # ln(x) = log(x, e)
    # human_age = (16 * (math.log(int(dog_age), math.e))) + 31 known best dog age formula
    # y = 8E-15x6 - 6E-11x5 + 1E-07x4 - 0.0002x3 + 0.0773x2 + 2.0835x equation for 0 - 6 years old
    # y = -0.0001x2 + 6.2952x equation for 6 - 30 years old (picked 30 years since oldest dog ever is 29)
    if dog_age < 0:
        print("Dog age must be greater than 0")
        return -1
    elif dog_age >= 0 and dog_age < 2191.455:
        human_age = ((8 * (10 ** -15)) * (float(dog_age) ** 6)) - ((6 * (10 ** -11)) * (float(dog_age) ** 5)) + \
                    ((1 * (10 ** -7)) * (float(dog_age) ** 4)) - (0.0002 * (float(dog_age) ** 3)) + \
                    (0.0773 * (float(dog_age) ** 2)) + (2.0835 * (float(dog_age)))
        return human_age
    elif dog_age >= 2191.455 and dog_age < 10957.275:
        human_age = (-0.0001 * (float(dog_age) ** 2)) + (6.2952 * float(dog_age))
        return human_age
    else:
        print("Dog age must be less than 30 years old")
        return -1

def x_vertex(a, b):
    xcoord = - b / (2 * a)
    return xcoord


def dog_human_intersect(human_age, dog_human_age):
    # polynomial ax^2 + bx + c
    # a
    a = -0.0001
    b = 5.2952
    c = human_age - dog_human_age
    # our equation has ax^2 + bx = c so we need to do -c
    xroots = roots([-0.0001, 5.2952, -c])
    # the only root we want is the x value before the peak of the parabola
    xvert = x_vertex(a, b)
    for root in xroots:
        if root < xvert:
            return root
        else:
            continue
    return -1

def dog_human_date(intersect, human_age, dog_age):
    today = date.today()
    same_age_date = today + timedelta(days=intersect)
    dog_new_age = dog_age + intersect
    human_new_age = human_age + intersect
    print("Your dog will be ", dog_new_age/365.2425, " years old")
    print("You will be ", human_new_age/365.2425, " years old")
    return same_age_date

#print(dog_to_human())
#print(dog_date_to_years())
dog_age = calculate_age_days()
print(dog_age)
dog_human_age = dog_to_human(dog_age)
print(dog_human_age)
dog_human_age2 = dog_to_human(3805)
print(dog_human_age2)
intersect = dog_human_intersect(21900, dog_human_age)
print(intersect)
human_same_age = dog_human_date(intersect, 21900, dog_age)
print(human_same_age)