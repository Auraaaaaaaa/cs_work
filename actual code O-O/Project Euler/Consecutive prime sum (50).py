targetnum = 999983

primes = []
for i in range(2, 999983):
    for j in range(2, i):
        if i % j == 0:
            break
        elif sum(primes) == targetnum:
            break
    else:
        primes.append(i)
print(primes)
print(sum(primes))