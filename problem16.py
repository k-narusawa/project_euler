# 215 = 32768 であり, 各位の数字の和は 3 + 2 + 7 + 6 + 8 = 26 となる.

# 同様にして, 21000 の各位の数字の和を求めよ.

num = 2 ** 1000

ans = num % 10
num = num // 10
while (num != 0):
    ans = ans + (num % 10)
    num = num // 10

print(ans)
