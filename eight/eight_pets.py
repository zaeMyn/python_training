# 定义为模块，删除此文件其他调用代码
def showAnimal(type,name):
    print("\nThis is "+type+",It's/Her/His name is "+name)
#
# # 位置实参
# showAnimal("Pig","piggy")
# # 关键字实参.不用关心位置
# showAnimal(type="Human",name="Marry")
# showAnimal(name="Mike",type="Human")
#
# 给形参指定默认值时， 等号两边不要有空格
# def showAnimalWithDefaultValue(type,name="Lily"):
#     print("\nThis is "+type+",It's/Her/His name is "+name)
# showAnimalWithDefaultValue(type="Human")
# # 请注意， 在这个函数的定义中， 修改了形参的排列顺序。 name 指定了默认值， 无需通过实参来指定动物类型， 因此在函数调用中只包含一个实参—-Animal的类型。
#
# #  然而， Python依然将这个实参视为位置实参， 因此如果函数调用中只包含动物的类型， 这个实参将关联到函数定义中的第一个形参。 这就是需要将type放在形参列表
# # 开头的原因所在。
# #等同于下面
# showAnimalWithDefaultValue("Bird")