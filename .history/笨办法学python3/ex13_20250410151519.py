# from sys import argv

# script,first,second,third=argv


# print("the script is called:",script)
# print("your first variable is:",first)
# print("your second variable is:",second)
# print("your thrid variable is:",third)

# #这里主要是argv是用于传递参数


#巩固练习
from sys import argv
script,option1,option2=argv
if option1==1 and option2==0:
    age=input("please input your age:")
    print(f"your age is {age}")
else:
    weight=input("please input your weight")
    print(f"you are {weight} heavy")