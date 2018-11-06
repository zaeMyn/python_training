'''根据约定， 在Python中， 首字母大写的名称指的是类'''
class Dog():
    """一次模拟小狗的简单尝试"""
    '''形参self 必不可少， 还必须位于其他形参的前面'''
    def __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name
        self.age = age
    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + " is now sitting.")
    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " rolled over!")