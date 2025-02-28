from pyexpat.errors import messages
from unicodedata import category


# contacts=["A","B","c","d","e"]
# for name in contacts:
#     message_content =name + ":Happy new year to you "+ name +\
#                      "wish you happy every day"
#     send_message(name,message_content)

#message_content ="""{0}
# {1}""".format(year,name) Number represents parameter substitution

#message_content ="""{year}
# {name}""".format(name=name,year=year) #You can use keywords without considering the order


#  gpa_dict = {A:3.251,"B":2.365,"C":3.12,\
#              "D":2.968}
#  for name , gpa in gpa_dict.items():
#      print("hello,{0},your gpa is :{1:.2f}".format(name,gpa))
# #                                   Keep two decimal places

def calculate_BMI (weight,height):
    BMI = weight / height ** 2
    if BMI <= 18.5:
        category = "Thin "
    elif 18.5< BMI <=25 :
        category = "Normal weight"
    elif BMI <=30 :
        category = "Overweight"
    else:
        category = "Obesity"
    print(f"Your weight type is:{category}") #f,You can use expressions directly in {}, not just variable names
    return BMI
result = calculate_BMI(70,1.5)#The function contains a return value function,\
                                            # so you can return something
print(result)
#calculate_BMI(70,1.5)


