# ピタゴラス数(ピタゴラスの定理を満たす自然数)とは a < b < c で以下の式を満たす数の組である.
# a2 + b2 = c2
# 例えば, 32 + 42 = 9 + 16 = 25 = 52 である.
# a + b + c = 1000 となるピタゴラスの三つ組が一つだけ存在する.
# これらの積 abc を計算しなさい.

x = 1000
flg = 0
for a in range(1, x):
    for b in range(a, x):
        for c in range(b, x):
            if(a**2+b**2 == c**2):
                if(a + b + c == 1000):
                    flg = 1
                    print(a, b, c)
                break
        if(flg == 1):
            break
    if(flg == 1):
        break
