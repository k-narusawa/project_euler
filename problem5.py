# 2520 は 1 から 10 の数字の全ての整数で割り切れる数字であり, そのような数字の中では最小の値である.
# では, 1 から 20 までの整数全てで割り切れる数字の中で最小の正の数はいくらになるか.

# x = 1
# i = 1
# while i < 21:
#     if (x % i != 0):
#         i = 1
#         x += 1
#         print(x)
#         continue
#     i += 1
# print(x)

max_num = 20
ans = 1

# 最大公約数 を求める（ユークリッドの互除法）


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# 最小公倍数 は a * b / gcd(a,b)


def lcm(a, b):
    return a * b // gcd(a, b)


# 指定の数まで、すべての最小公倍数を求める
for i in range(1, max_num + 1):
    ans = lcm(i, ans)

print(ans)
