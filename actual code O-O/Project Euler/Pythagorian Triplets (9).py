def get_triplet():
    for c in range(2, 1000):
        for b in range(2, c):
            a = 1000 - c - b
            if a ** 2 + b ** 2 == c ** 2:
                return 'n1 = %s\nn2 = ' \
                       '%s\nn3 = %s\nproduct = %s' \
                       % (a, b, c, a * b * c)


if True:
    print(get_triplet())