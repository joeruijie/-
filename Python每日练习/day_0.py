#coding=utf-8
"""
定义两个变量 x 、 Y, 分别赋值 3 、 5 ，用eval()函数计算 x 的 y 次方的值
eval是Python的一个内置函数，这个函数的作用是，返回传入字符串的表达式的结果。
"""
x = 3
y = 5
print(eval('x**y'))
x = eval(input("请输入x的值："))
y = eval(input("请输入y的值："))
print(x**y)