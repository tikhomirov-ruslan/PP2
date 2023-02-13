# 1
# grams = float(input())
def ounces(grams):
    return 28.3495231 * grams
# print(ounces(grams))

# 2
# F = float(input())
def Celsius(F):
    return (5 / 9 * (F - 32))
# print(Celsius(F))

# 3
numheads = 35
numlegs = 94
def solve(numheads, numlegs):
    rabbits = (numlegs - numheads * 2) / 2
    chickens = numheads - rabbits
    return [rabbits , chickens]

# 4
def isPrime(x):
    if x == 1:
        return False
    d = 2
    while x % d != 0 and pow(d, 2) < x:
        d += 1
    if x % d == 0:
        return False
    else: 
        return True
def filterPrime(list):
    return list(filter(isPrime, list))
