# 所有的import 语句都应放在文件开头， 唯一例外的情形是， 在文件开头使用了注释来描述整个程序
# 第一种引入模块方法方式
from eight import eight_user_profile, eight_user_profile as userProfile

user_profile = userProfile.build_profile('albert', 'einstein',
    location='princeton',
    field='physics')
print(user_profile)

user_profile = eight_user_profile.build_profile('albert', 'einstein',
                                                location='princeton',
                                                field='physics')
print(user_profile)
# 第二种引入指定方法的方式
from eight.eight_pets import showAnimal
showAnimal("Pig","piggy")
#指定方法别名，防止冲突
from eight.eight_pets import showAnimal as showAnimal2
showAnimal2("Pig","piggy")

from nine.dog import Dog as littleDog
my_dog = littleDog('willie', 6)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

# from nine.car import Car as myCar
# # from nine.electricCar import ElectricCar as myElectricCar
from nine.car import Car as myCar
from nine.electricCar import ElectricCar as myElectricCar
#引入同个文件中的不同类
from nine.car import Car2 as ParentCar2,Car as car2

myCar = myCar('BMW','B8',2018)
print(myCar.get_descriptive_name())
myCar.odometer_reading = 240
myCar.read_odometer()
myCar.update_odometer(111)
myCar.read_odometer()
myCar.increment_odometer(100)
myCar.read_odometer()

myElectricCar = myElectricCar('Audi','A8',2019)
print(myElectricCar.get_descriptive_name())
myElectricCar.battery.describe_battery()
myElectricCar.battery.battery_size = 88;
myElectricCar.battery.describe_battery()

#引入整个模块的所有类，并重命名模块名
import nine.car as carModule
# 与下面的方式相同，但不推荐。存在冲突，不清楚含有哪些类的问题
from  nine.car import *
myCarModule = carModule.Car('BMW','B8',2018)
print('myCarModule:'+myCarModule.get_descriptive_name())