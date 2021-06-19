pre = 1
sfx = 2
fib = 0
sum = 2
while(fib <= 4000000):
    fib = pre+sfx
    tmp = pre
    pre = sfx
    sfx += tmp
    if not(fib % 2):
        sum += fib

print(sum)
