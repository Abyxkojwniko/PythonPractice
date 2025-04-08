print("how old are you", end = " ")
age=input() 
print("how tall are you", end = " ")
height=input()
print("how much do you weight", end = " ")
weight=input()
print(f"so,you're {age} old,{height} tall and {weight} heavy")
#这里请注意，如果要提示python使用前面定义的变量为后面的语句赋值
#应当在前方加f或者在后方加入.format