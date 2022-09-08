number = 15
factor = 2

while number > 1:
    if number % factor == 0:
        print(factor)
        number = number // factor
    else:
        factor = factor + 1
