# ~ 判断数字
answer = 12
if answer != 20:
    print("数不为20")
if answer > 15 and answer <20:
    print("数在15-20之间（不包含首尾数字）")
if (answer > 15) and (answer <20):
    print("数在15-20之间（不包含首尾数字）")
if (answer > 15) or (answer <10):
    print("数小于10，或者大于15")
else:
    print("数既不小于10，也不大于15")
