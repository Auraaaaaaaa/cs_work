n = 13
max_length = [0,0]
ipo = 0
count = int(0)


def colantz(n,count=1):
    while n > 1:
        count += 1
        if n%2 == 0:
            n=n/2
        else:
            n= (3*n) +1
    return count

for i in range(1000000):
    ipo = colantz(i)
    if ipo > max_length[0]:
        max_length[0] = ipo
        max_length[1] = i

print(max_length)