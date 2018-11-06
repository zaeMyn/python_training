from random import randint
# x = randint(1, 6)
print('打印1-16之间的整数10次')
for i in range(0,11):
    print(randint(1, 6))
i = 0
print('\n打印1-10之间的整数10次')
while i< 10:
    print(randint(1, 10))
    i=i+1
print('\n打印1-20之间的整数10次')
i = 0
while i< 10:
    print(randint(1, 20))
    i=i+1