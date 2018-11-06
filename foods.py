# ~ 复制，切片才能添加各自不同的内容.
# ~ 不是切片会同时映射，导致内容一样。
my_foods = ['Rice','Pizza','Fish']
my_foods2 = ['Rice','Pizza','Fish']
# ~ 不使用切片
friend_foods = my_foods
my_foods.append('Cake')
friend_foods.append('Bread')
# ~ 使用切片
friend_foods2 = my_foods2[:]
my_foods2.append('Coffe');
friend_foods2.append('Sandwich');
print(my_foods)
print(friend_foods)
print("\n")
print(my_foods2)
print(friend_foods2)
for food in friend_foods2[0:2]:
    print(food)
