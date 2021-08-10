# The String Data Type
myStr = "This a string"
print(myStr,"\n",type(myStr))
print(myStr,"is of data type",type(myStr))
# String Concatenation
str1, str2 = "water", "fall"
str3 = str1 + str2
print(str3)
# Input String
name = input("What is your name? ")
print(name)
# Format Output String
color = input("What is your favorite color? ")
animal = input("What is your favorite animal? ")
print("{}, you like a {} {}!".format(name,color,animal))