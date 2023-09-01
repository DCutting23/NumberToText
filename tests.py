import NumberToText

for i in range(1,999999999):
    digits = []
    num = str(i)
    for char in num:
        digits.append(char)
    print(NumberToText.millions(digits))