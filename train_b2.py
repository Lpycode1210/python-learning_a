# user_weight =float(input("please input your weight(kg):"))
# user_height =float(input("please input your height (m):"))
# user_BMI    =user_weight/(user_height)**2
# print("your BMI is"+str(user_BMI))#print need same form /format
# if user_BMI <=18.5:
#     print("you are underweight")
# elif (user_BMI>18.5)and(user_BMI<=25):#elif add brackets or18.5<user_BMI<=25
#     print("your weight is normal ")
# elif 25< user_BMI <=30:#elif (user_BMI>25)and(user_BMI<=30):But don't forget the conditional end symbol
#     print("you are overweight")
# elif (user_BMI>30):# or else:
#     print("your weight is obese,please pay attention to your diet")



#if you want to determine a multiple condition ,and use if perform multiple nesting operations that very complex
#there is logical operation and  or  not  priority not>and>or  but you can use() change them order

# # Define variables
# is_raining = True
# is_cloudy = False
# have_umbrella = False
# is_going_out = True

# 提示用户输入四个条件的值
is_raining = input("Is it raining? (Ture/False): ")
is_cloudy = input("Is it cloudy? (Ture/False): ")
have_umbrella = input("Do you already have an umbrella? (Ture/False): ")
is_going_out = input("Are you going out? (Ture/False): ")


# Nested if statements to decide whether to take an umbrella
if is_going_out:
    if is_raining:
        if not have_umbrella:
            print("You should take an umbrella because it is raining and you don't have one.")
        else:
            print("You don't need to take an umbrella because you already have one.")
    elif is_cloudy:
        print("You should take an umbrella because it might rain.")
    else:
        print("You don't need to take an umbrella because it is not raining and not cloudy.")
else:
    print("You don't need to take an umbrella because you are not going out.")


#use and or not
# Define variables
# is_raining = True
# is_cloudy = False
# have_umbrella = False
# is_going_out = True
#
# # Using logical operators to decide whether to take an umbrella
# if is_going_out and is_raining and not have_umbrella:
#     print("You should take an umbrella because it is raining and you don't have one.")
# elif is_going_out and is_raining and have_umbrella:
#      print("You don't need to take an umbrella because you already have one.")
# elif is_going_out and is_cloudy:
#     print("You should take an umbrella because it might rain.")
# elif is_going_out and not (is_raining or is_cloudy):
#     print("You don't need to take an umbrella because it is not raining and not cloudy.")
# else:
#     print("You don't need to take an umbrella because you are not going out.")