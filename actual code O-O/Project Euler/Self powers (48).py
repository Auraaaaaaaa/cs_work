numsarray = []
num = 1
numans = 0
arraysum = 0
for i in range(1, 1001):
    numans = num ** num
    numsarray.append(numans)
    num += 1
numans = str(sum(numsarray))[-10:]
print(numans)