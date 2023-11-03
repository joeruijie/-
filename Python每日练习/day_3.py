
"""
程序自动生成一个数，0~10之间，用户猜测产生的数，如果大于产生的数，就显示太大了，否则就太小了，用户循环N次，
直到成功猜对数字，猜对了显示猜对了
当用户输入不是整数时，显示用户输入必须是整数才可以继续

"""
import random
auto_num = random.randint(0,10)

count = 1
while True:
    cin_num = int(input("请输入一个数字："))
    if cin_num % 1 != 0:
        print("输入必须是整数")
        cin_num = int(input("请输入一个数字："))
        continue
    if cin_num == auto_num:
        print("猜对了", '只用了', count, '次!')
        break
    elif cin_num > auto_num:
        print("太大了")
    elif cin_num < auto_num:
        print("太小了")
    count += 1
