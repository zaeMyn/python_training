import unittest
from eleven.name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """测试name_function.py"""
    def test_first_last_name(self):
        """能够正确地处理像Janis Joplin这样的姓名吗？ """
        formatted_name = get_formatted_name('janis', 'joplin')
        print('test_first_last_name打印内容：'+formatted_name)
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """能够正确地处理像Wolfgang Amadeus Mozart这样的姓名吗？ """
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        print('test_first_last_middle_name打印内容：' + formatted_name)
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')
# unittest.main()
print("__name__:"+__name__+'\n')
if __name__ == '__main__':
    unittest.main()