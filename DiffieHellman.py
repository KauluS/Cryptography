import random
import primeTest

p = 0

### pが素数になるまでランダムに生成し続ける
# ミラー・ラビン素数判定法
while not primeTest.MillerRabin(p, 50):
    p = random.randint(1<<500, 1<<1000)
    continue

# 平方根を利用した素数判定法
# while not primeTest.Sqrt(p, 50):
#     p = random.randint(1<<500, 1<<1000)
#     continue

alpha = random.randint(2, p-1) # 上記で得た素数から, 2 <= alpha < pを満たすランダムなalphaを生成

x1 = random.randint(0, p-2)
y1 = primeTest.modPow(alpha, x1, p)

x2 = random.randint(0, p-2)
y2 = primeTest.modPow(alpha, x2, p)

k1 = primeTest.modPow(y2, x1, p)
k2 = primeTest.modPow(y1, x2, p)

print('k1: ' + str(k1))
print()
print('k2: ' + str(k2))