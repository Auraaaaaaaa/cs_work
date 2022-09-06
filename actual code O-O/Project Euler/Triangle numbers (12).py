num = 0

def isTriangle(n):
    for i in range(1,n):
        if (i*(i+1)/2) == n:
            return True
    return False