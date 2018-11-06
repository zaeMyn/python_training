from nine.car import Car as ParentCar
from nine.battery import Battery as battery
# 继承自Car类
class ElectricCar(ParentCar):
    def __init__(self, make, model, year):
        """初始化父类的属性"""
        super().__init__(make, model, year)
        # 将实例用作属性
        self.battery = battery();
        # self.battery = battery(55);

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name ='Child:'+str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()