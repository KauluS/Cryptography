import math
import random

# 平方根を利用した素数判定法
def Sqrt(p):
    if 0 == p % 2:
        return False
    
    i = 5
    while p >= i * i:
        if 0 == p % i or 0 == p % (i+2):
            return False
        i += 6

    return True

# ミラー・ラビン素数判定法
def MillerRabin(p, t):
    if 1 >= p: return False

    if 2 == p: return True
    
    d = (p - 1) // 2
    while 0 == d % 2:
        d = d >> 1
    s = int(math.log(((p-1) / d), 2))

    i = 1
    while True:
        a = random.randint(2, p-1)
        b = modPow(a, int(d), p)
        j = 0
        while s > j and 1 != b and p - 1 != b:
            b = (b ** 2) % p
            j += 1

        if s == j or (0 < j and 1 == b):
            return False
        
        if t == i:
            return True
        
        i += 1

# a**bをmで割った余りを返す
def modPow(a, b, m):
    res = 1
    while 0 < b:
        if 1 == b % 2:
            res *= a
            res %= m
        a *= a
        a %= m
        b = b >> 1
    return res