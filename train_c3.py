#Perform actions when errors occur
try:
    user_weight = float(input("Please enter your weight(kg):"))
    user_height = float(input("Please enter your height( m ):"))
    user_BMI = user_weight/user_height**2
except ValueError:
    print("The input number is unreasonable. Please re-enter the correct number")
    #If this kind of error occurs, print this sentence

except ZeroDivisionError:
    print("Height cannot be 0. Please run the program again and enter a reasonable height value")
    # If this kind of error occurs, print this sentence

    #but When multiple errors occur, only the first one can be displayed---just ValueError
except:
    print("There is an unknown error, please run again and enter a reasonable value")
    #When you do not know what error will occur, you can directly use: except:

else:
    print("your BMI is "+ str(user_BMI))
    #if Run this if there are no errors

finally:
    print("Program end run")
    #This will be executed with or without errors


# assert len("Hi")==2
# assert 1+2 > 6
# assert "a" in ["b","c"]
#Using the assert statement, if the subsequent program is not true, the assertion error will be returned.
# Later programs will stop executing


#独立文件
# import unittest 验证是否符合预期
# from my_calculator import my_adder 引入文件里写到的
# class TestMyAdder(unittest.TestCase):  创建一个类，需要是unittest.TestCase的子类。继承unittest.TestCase中的各种测试功能

#     def test_positive_with_positive(self):只把test_开头的当作测试
#         self.asserEqual(my_adder(5,3)8)    测试引入的my_adder函数3+5=8正确否，如果不对后面的还能运行检查asserEqual测试加法
#asserNotEqual 测试不相等。assertTure(A)也是一种测试方法等等.....
#     def test_negative_with_positive(self):
#         ...


#高阶函数
#匿名函数 lambda num1,num2:num1 + num2 只能够有一个语句表达式.







