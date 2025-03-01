#Learning object oriented
#1
# class CuteCat:
#     def __init__(self,cat_name):
#          self.name = cat_name
#
# cat1 = CuteCat("jojo")
# print(cat1.name)

#2
class CuteCat:
    def __init__(self,cat_name,cat_age,cat_color):
        self.name=cat_name
        self.age =cat_age
        self.color=cat_color
cat1=CuteCat("jojo",2,"blue")
print(f"{cat1.name} is a {cat1.color} cat,it's {cat1.age} years old")