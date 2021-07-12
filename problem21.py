# d(n) を n の真の約数の和と定義する. (真の約数とは n 以外の約数のことである. )
# もし, d(a) = b かつ d(b) = a (a ≠ b のとき) を満たすとき, a と b は友愛数(親和数)であるという.

# 例えば, 220 の約数は 1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110 なので d(220) = 284 である.
# また, 284 の約数は 1, 2, 4, 71, 142 なので d(284) = 220 である.

# それでは10000未満の友愛数の和を求めよ.

def yaku_sum(num):
    divisors = []
    for i in range(1, int(num**0.5)+1):
        if num % i == 0:
            divisors.append(i)  # 約数をリストに追加
            if i**2 == num:  # 重解の場合に2つリストされるのを防ぐ
                continue
            divisors.append(num//i)  # 約数の相手方をリストに追加
#     return divisors         #昇順にしなくてよいならソートは不要
    x = sorted(divisors)  # 昇順にしたいときはソートする
    x.pop(-1)
    return sum(x)


def yuuai(n):
    b = yaku_sum(n)
    a = yaku_sum(b)
    print(a, n)
    if a == n and a != b:
        return True
    return False


ans = 0
for i in range(2, 10001):
    if yuuai(i):
        ans += i

print(ans
      )
