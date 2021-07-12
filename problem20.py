# n × (n - 1) × ... × 3 × 2 × 1 を n! と表す.

# 例えば, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800 となる.
# この数の各桁の合計は 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27 である.

# では, 100! の各位の数字の和を求めよ.

def kaijou(n):
    ans = 1
    for i in range(1, n+1):
        ans = ans * i
    return ans


def digit_sum(n):
    ans = 0
    while(True):
        ans += n % 10
        n = n // 10
        if n == 0:
            break
    return ans


print(digit_sum(kaijou(100)))
