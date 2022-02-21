import math

for i in range(3):
    a = int(input("Input a: "))
    b = int(input("Input b: "))
    x = int(input("Input x: "))

    one_b2 = 1 / pow(b, 2)
    expression = 2 * x - 1
    ln = math.log(expression)
    sum_of_values = (5 * a / expression) - (7 * pow(a, 2) / pow(expression, 2)) + (10 * pow(a, 3) / 3 * pow(expression, 3)) - (7 * pow(a, 4) / 4 * pow(expression, 4))
    result = one_b2 * sum_of_values

    print("Result: ", end="")
    print("%.2f" % result)

    i+=1