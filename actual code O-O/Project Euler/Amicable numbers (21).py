amicable_numbers = []

def find_proper_divisors(n):
    proper_divisors = []
    for i in range(1, n):
        if n % i == 0:
            proper_divisors.append(i)
    return proper_divisors
def find_amicable_pair(n):
    sum_of_proper_divisors = sum(find_proper_divisors(n))
    sum_of_proper_divisors_of_sum_of_proper_divisors = sum(find_proper_divisors(sum_of_proper_divisors))
    if sum_of_proper_divisors_of_sum_of_proper_divisors == n:
        return n, sum_of_proper_divisors
    else:
        return None
for i in range(1, 10000):
    if find_amicable_pair(i) != None:
        amicable_numbers.append(find_amicable_pair(i))
#split the tuples into two lists
amicable_numbers_1 = []
amicable_numbers_2 = []
for i in range(len(amicable_numbers)):
    amicable_numbers_1.append(amicable_numbers[i][0])
    amicable_numbers_2.append(amicable_numbers[i][1])
#sum both arrays
print(sum(amicable_numbers_1) + sum(amicable_numbers_2))