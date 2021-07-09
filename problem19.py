# 次の情報が与えられている.

# 1900年1月1日は月曜日である.
# 9月, 4月, 6月, 11月は30日まであり, 2月を除く他の月は31日まである.
# 2月は28日まであるが, うるう年のときは29日である.
# うるう年は西暦が4で割り切れる年に起こる. しかし, 西暦が400で割り切れず100で割り切れる年はうるう年でない.
# 20世紀（1901年1月1日から2000年12月31日）中に月の初めが日曜日になるのは何回あるか?
def uruu(year):
    if year % 4 == 0:
        if year % 400 != 0 and year % 100 == 0:
            return False
        return True
    return False


def print_calender(count):
    for d in range(1, month2[m-1] + 1):
        print(d, end='')
        if date == 1 and d == 1 and y != 1901:
            print(str(y) + " " + str(m) + " " + str(d))
            count += 1
        if date == 7:
            date = 1
            print()
        else:
            date += 1
    print()


month1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month2 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
date = 1
count = 0

for y in range(1900, 2001):
    if uruu(y):
        for m in range(1, 13):
            print(str(m) + '月')
            for d in range(1, month2[m-1] + 1):
                print(d, end='')
                if date == 1 and d == 1 and y != 1901:
                    print(str(y) + " " + str(m) + " " + str(d))
                    count += 1
                if date == 7:
                    date = 1
                    print()
                else:
                    date += 1
    else:
        for m in range(1, 13):
            print(str(m) + '月')
            for d in range(1, month1[m-1] + 1):
                print(d, end='')
                if date == 1 and d == 1 and y != 1901:
                    print(str(y) + " " + str(m) + " " + str(d))
                    count += 1
                if date == 7:
                    date = 1
                    print()
                else:
                    date += 1


print(count)
print(uruu(1900))
