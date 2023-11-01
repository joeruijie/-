#coding=utf-8
import math
"""
用 f 字符串格式化输出：计算 365 天进行学习积累与放任怠惰后的知识储备
"""
#方法一
up = 1.01
day = 365
down = 0.99
knowledge = up ** day
xiedadi = down ** day
print(f"计算 {day} 天进行放任怠惰后的知识储备：{xiedadi}")
print(f"计算 {day} 天进行学习积累后的知识储备：{knowledge}")
#方法二
#pow 要传2个值，x和y，对应x**y
#学习365天
action =math.pow((1+0.01),365)
#懈怠365天
lazy = math.pow((1-0.01),365)
print(f"计算 {day} 天进行放任怠惰后的知识储备：{lazy:.2f}")
print(f"计算 {day} 天进行学习积累后的知识储备：{action:.2f}")
#计算三天打鱼2天筛网
#3天打鱼

fish = math.pow((1+0.01),3)
#2天筛网

net = math.pow((1-0.01),2)
#1年的结果
result = math.pow((fish*net),(365/5))
print(f"计算三天打鱼2天筛网后的结果：{result:.2f}")