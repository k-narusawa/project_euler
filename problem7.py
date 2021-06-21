# 素数を小さい方から6つ並べると 2, 3, 5, 7, 11, 13 であり, 6番目の素数は 13 である.

# 10 001 番目の素数を求めよ.

def getPrime(num):
    i = 2
    ans = []
    while len(ans) < num:
        for j in range(2, i+1):
            if(i != j and i % j == 0):
                break
            if(j == i):
                ans.append(j)
        i += 1
    return ans


print(getPrime(10001))
