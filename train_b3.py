shopping_list = []
shopping_list.append("keyboard")#[]It can store different data types
shopping_list.append("pencil")
shopping_list.append(2)
shopping_list[1]="你好"#If it is not quoted, it is a variable, but if you do not define it, you will make an error
# #Overwrite original position
len(shopping_list)
print(shopping_list[1],len(shopping_list))#print second element
number_list=[-6,8,2,-10,9,1]#Comma is used to separate and coordinate
print(max(number_list),"\n",sorted(number_list),"\n",min(number_list))#Commas have spaces by default
shopping_list.remove(shopping_list[1])
print(shopping_list)