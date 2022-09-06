def find_prime():
    prime_to_find  = 10001
    list_primes = []
    x = 2
    while(len(list_primes) < prime_to_find): 
        if all(x % prime for prime in list_primes): 
            list_primes.append(x)
        x +=1
    print(list_primes[-1])
find_prime()
