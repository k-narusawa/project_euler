# 1 から 5 までの数字を英単語で書けば one, two, three, four, five であり, 全部で 3 + 3 + 5 + 4 + 4 = 19 の文字が使われている.

# では 1 から 1000 (one thousand) までの数字をすべて英単語で書けば, 全部で何文字になるか.

# 注: 空白文字やハイフンを数えないこと. 例えば, 342 (three hundred and forty-two) は 23 文字, 115 (one hundred and fifteen) は20文字と数える. なお, "and" を使用するのは英国の慣習.

num_dict = {
    0: '',
    1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
    6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
    11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
    17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty',
    40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'
}

ans = 0
ans += len('onethousand')

for i in range(1000):
    if i > 99:
        ans += len(num_dict[i // 100])
        ans += len('hundred')
        if i % 100 > 0:
            ans += len('and')

    tmp_i = i % 100
    if tmp_i in num_dict:
        ans += len(num_dict[tmp_i])
    else:
        ans += len(num_dict[(tmp_i // 10) * 10])
        ans += len(num_dict[tmp_i % 10])

print(ans)
