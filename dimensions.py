# ~ 元组，不可变，通过索引访问。使用圆括号赋值，方括号取值
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])
print("\n")
# ~ 遍历元组跟遍历列表一样
for dimension in dimensions:
    print(dimension)
print("\n")
# ~ 虽然不能修改元组的元素， 但可以给存储元组的变量赋值。 因此， 如果要修改前述矩形的尺寸， 可重新定义整个元组
dimensions = (240,500)
for dimension in dimensions:
    print(dimension)
