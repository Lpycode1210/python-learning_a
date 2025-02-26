# #Use a dictionary to store data pairs
# slang_dict={"red":"256",
#             "blue":"512",
#             "yellow":"1024",
#             "yyds":"永远的神"}
# #{}Store a pair of data
# slang_dict["xswl"]="笑死我了"
# slang_dict["jjz"]="绝绝子"
# word = input ("Please enter the information you want to get:")
# #mean=slang_dict[word] if add hear,all of words
# if word in slang_dict:
#     mean = slang_dict[word]
#     print("It means "+ mean)
# else:
#     print("There are no words in the dictionary you are looking for."+"Here are"+str(len(slang_dict)) +"words")
#     # len() The data type for length is not a string. It needs to be converted to a string for splicing

# temperature_dict={"111":36.4,"112":36.6,"113":36.2}
# for staff_id,temperature in temperature_dict.items():#for+variate from next
#     if temperature>=36.5:
#         print(staff_id + " : " +str(temperature))


#range(5,10) 5,6,7,8,9 nonentity 10
#range(5,10,2) 2 is stride
add=0
for i in range(1,101):
    add = add + i
print(add)#If indented, it exists in the for loop and will be printed every time.
# If not indented(缩进), only the value at the end of the last loop will be printed

