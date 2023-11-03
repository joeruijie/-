"""
绘制一个等边三角形，并且填充颜色
"""
import turtle

turtle.setup(500,300)
turtle.pensize(3)
turtle.pencolor('black')
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor('red')
turtle.goto(40,0)
turtle.left(120)
turtle.forward(80)
turtle.left(120)
turtle.forward(80)
turtle.left(120)
turtle.forward(40)
turtle.end_fill()
turtle.hideturtle()
turtle.exitonclick()