class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        """ 默认属性值"""
        '''""" 默认属性值"""'''
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """将里程表读数设置为指定的值"""
        self.odometer_reading = mileage

    def increment_odometer(self, miles):
        """将里程表读数增加指定的量"""
        self.odometer_reading += miles
class Car2():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        """ 默认属性值"""
        '''""" 默认属性值"""'''
        self.odometer_reading = 0
