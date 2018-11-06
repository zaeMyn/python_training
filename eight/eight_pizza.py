def make_pizza(*toppings):
    for value in toppings:
        print(value)
    length = len(toppings)
    print('长度：'+str(length)+',最后一个值是：'+str(toppings[length-1]))

make_pizza('pppp')
make_pizza('1',1,34)