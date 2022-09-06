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
num = 1
numarray = []
while num <=2000000:
    if isprime(num):
        numarray.append(num)
        print(num)
    num = num + 2
print(sum(numarray))