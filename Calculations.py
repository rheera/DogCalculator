from numpy import roots

def x_vertex(a, b):
    xcoord = - b / (2 * a)
    return xcoord


ans = roots([-0.0001, 5.2952, -6457])
vert = x_vertex(-0.0001, 5.2952, -6457)
print("the x vert is: ",  vert)
for value in ans:
    print(value)

for value in ans:
    if value < vert:
        print("Your x is: ", value)
    else:
        continue

print(roots([-0.0001, 5.2952, -6457]))
dog_age = 2920
human_age = (4.5 * float(dog_age)) + 5566.3
print(human_age)
print(human_age/365.2425)