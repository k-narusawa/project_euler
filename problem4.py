# 左右どちらから読んでも同じ値になる数を回文数という. 2桁の数の積で表される回文数のうち, 最大のものは 9009 = 91 × 99 である.
# では, 3桁の数の積で表される回文数の最大値を求めよ.

kaibun = 1
max = kaibun
for i in range(1, 1001):
    for j in range(1, 1001):
        kaibun = i*j
        x = str(kaibun)
        reverse = ''.join(reversed(x))
        if(x == reverse and kaibun > max):
            max = kaibun
print(max)

max_num = 1000
max_ans = 0
for i in range(100, max_num):
    for j in range(i, max_num):
        num = i * j
        num_str = str(num)
        # str[::-1] で反転。str[i:j:k] は i to j step by k
        if num_str == num_str[::-1] and num > max_ans:
            max_ans = num
print(max_ans)
