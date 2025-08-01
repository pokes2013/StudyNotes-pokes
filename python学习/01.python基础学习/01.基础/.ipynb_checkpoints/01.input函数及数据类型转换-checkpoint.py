# 由计算机提问而得到的任何回答都是字符串类型
age=input('你几岁了？')
print(age)
print(type(age))
age=int(age)     #数据类型转换
print(type(age))