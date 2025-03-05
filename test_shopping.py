# #Write a test program for this class-c1
# import unittest
# from train_c1 import ShoppingList
# class TestShoppingList(unittest.TestCase):
#      def setUp(self):
#          self.shopping_list=ShoppingList({"纸巾":8,"帽子":30,"拖鞋":15})
#      def test_get_item_count(self):
#          #shopping_list=ShoppingList({"纸巾":8,"帽子":30,"拖鞋":15})
#          self.assertListEqual(self.shopping_list.get_item_count(),3)
#
#      def test_get_total_price(self):
#          #shopping_list = ShoppingList({"纸巾": 8, "帽子": 30, "拖鞋": 15})
#          self.assertListEqual(self.shopping_list.get_total_price(),53)
# if __name__ == '__main__':
#     unittest.main()


#独立文件
# import unittest 验证是否符合预期
# from my_calculator import my_adder 引入文件里写到的
# class TestMyAdder(unittest.TestCase):  创建一个类，需要是unittest.TestCase的子类。继承unittest.TestCase中的各种测试功能

#     def test_positive_with_positive(self):只把test_开头的当作测试
#         self.asserEqual(my_adder(5,3)8)    测试引入的my_adder函数3+5=8正确否，如果不对后面的还能运行检查asserEqual测试加法
#asserNotEqual 测试不相等。assertTure(A)也是一种测试方法等等.....
#     def test_negative_with_positive(self):
#         ...




import unittest
from train_c1 import ShoppingList


class TestShoppingList(unittest.TestCase):
    def setUp(self):
        self.shopping_list = ShoppingList({"纸巾": 8, "帽子": 30, "拖鞋": 15})

    def test_get_item_count(self):
        self.assertEqual(self.shopping_list.get_item_count(), 3)

    def test_get_total_price(self):
        self.assertEqual(self.shopping_list.get_total_price(), 53)

