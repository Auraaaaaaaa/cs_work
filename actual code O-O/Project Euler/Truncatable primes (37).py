from algorithms import *
ptestnum = 2
primes = []
def isprime(num):
    flag = False
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                flag = True
                break
    if flag:
        return False
    else:
      return True
while ptestnum < 10000000:
    #check if ptestnum is prime
    if isprime(ptestnum):
        primes.append(ptestnum)
    ptestnum += 2


def is_truncatable_right(n):
    a = True
    if n > 10:
        for x in range(len(str(n))):
            if int(n) not in primes:
                a = False
            n = str(n)[:-1]
        return a
    else:
        return False


def is_truncatable_left(n):
    a = True
    if n > 10:
        for x in range(len(str(n))):
            if int(n) not in primes:
                a = False
            n = str(n)[1:]
        return a
    else:
        return False


def main():
    n = []
    a = 11
    while len(n) != 11:
        if is_truncatable_left(a) and is_truncatable_right(a):
            n.append(a)
        a += 1
    return n, sum(n)


print(main())