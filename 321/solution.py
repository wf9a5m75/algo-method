import math
def isPrime(N):
    if N < 3:
        if N > 1:
            return True
        return False
    if (N & 1 == 0) or (N % 3 == 0):
        return False

    upper = math.sqrt(N)

    i = 5
    while(i <= upper):
        if (N % i == 0) or (N % (i + 2) == 0):
            return False
        i += 6
    return True

i = 53
while(i < 100):
    i += 2
    if (i % 3 != 0) and isPrime(i):
        print(i)
        break
