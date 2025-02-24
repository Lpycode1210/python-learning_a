#BMI=weight/(height**2)
from urllib.parse import uses_relative
#
# user_weight =input("please imput your weight(kg):")
# user_height =input("please imput your height (m):")
# #user_BMI    =user_weight/(user_height)**2  #These two are strings. Mathematical operations cannot be performed
# print(suer_BMI)



# user_weight =float(input("please imput your weight(kg):"))
# user_height =float(input("please imput your height (m):"))
# user_BMI    =user_weight/(user_height)**2
#
# #print("your BMI is"+user_BMI)#user_BMI is number we need change to str
# print("your BMI is"+str(user_BMI))#print need same form /format

mood_index=int(input("your friend rank of mood is :"))
if mood_index >=60:
    print("you can play game tonight")
elif (mood_index<60)and (mood_index>=50):
    print("just so")
elif (mood_index>=40) and (mood_index<50):
    print("no")
else:  #mood_index <40
    print("his/her mood is bad ,and you can't play game")
