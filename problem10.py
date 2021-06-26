def isPrime(num):
# 2は素数
  if(num==2): 
    return True

# 偶数は合成数
  if(num%2==0):
    return False

# 素数判定は平方根までで良い
  for i in range(2, int(num**0.5) + 1):
    if(num%i == 0):
      return False
  return True

ans = 0
val = 2000000
for i in range(2, val):
  print(i)
  if(isPrime(i)):
    ans += i

print(ans)