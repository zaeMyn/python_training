requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")
for requested in requested_toppings:
    print("Add "+requested +" in pizza")
requested_toppings = []
# 判断是否为空
if requested_toppings:
    print("不为空")
else:
    print("没有配料啊")

