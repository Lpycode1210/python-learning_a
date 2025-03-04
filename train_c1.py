# class ShoppingList:
#     def __init__(self,shopping_list):
#         self.shopping_list = shopping_list
#     def get_item_cpunt(self):
#         return len(self.shopping_list)
#     def get_total_price(self):
#         total_price = 0
#         for price in self.shopping_list.values():
#             total_price+= price
#         return total_price
#


#
# f=open("./data.txt","r",encoding="utf-8")#1地址  2模式（r只读）3编码方式UTF-8
# content=f.read()#read(10) read 1-10 字节内容 next read(10) 11-20
# print(content)
# f.close()#释放资源
# #with open("./data.txt") as f:#自动关闭



with open("./data.txt","a",encoding="utf-8") as f:#w写入，如果文件存在内容会清空内容。a则是附加内容
    f.write("Hello!\n")
    f.write("word\n")
        
