"""

·输入三条边长，判断能否构成三角形·注：两边之和大于第三边则可构成三角形
"""
def triangle(a,b,c):
    while True:
        if a+b>c and a+c>b and b+c>a:
            print('可以构成三角形')
            break
        else:
            print('不能构成三角形')
            break


if __name__ == '__main__':
    a = int(input('请输入第一条边长：'))
    b = int(input('请输入第二条边长：'))
    c = int(input('请输入第三条边长：'))
    triangle(a,b,c)