# 2×2 のマス目の左上からスタートした場合, 引き返しなしで右下にいくルートは 6 つある.


# では, 20×20 のマス目ではいくつのルートがあるか.

# (縦の移動数+横の移動数)! / (縦の移動回数)!(横の移動回数)!

def kaijo(n):
    ans = 1
    for i in range(1, n+1):
        ans *= i
    return ans


num = kaijo(40) / (kaijo(20) * kaijo(20))

print(num)
