"""
绘制国旗:
先将旗面划分为4个等分长方形，再将左上方长方形划分长宽15×10个方格。
大五角星的中心位于该长方形上5下5、左5右10之处。大五角星外接圆的直径为6单位长度。
四颗小五角星的中心点，第一颗位于上2下8、左10右5，
第二颗位于上4下6、左12右3，第三颗位于上7下3、左12右3，
第四颗位于上9下1、左10右5之处。
每颗小五角星外接圆的直径均为2单位长度。四颗小五角星均有一角尖正对大五角星的中心点。
"""

import turtle


def draw_rectangle(x,y,width,height):
    turtle.goto(x,y)
    turtle.pencolor("red")
    turtle.fillcolor("red")
    turtle.begin_fill()

    for i in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()

def draw_star(x,y,radius):
    turtle.setpos(x,y)
    pos1 = turtle.pos()
    turtle.circle(-radius,72)
    pos2 = turtle.pos()
    turtle.circle(-radius,72)
    pos3 = turtle.pos()
    turtle.circle(-radius,72)
    pos4 = turtle.pos()
    turtle.circle(-radius,72)
    pos5 = turtle.pos()    
    turtle.color('yellow','yellow')
    turtle.begin_fill()
    turtle.goto(pos3)
    turtle.goto(pos1)
    turtle.goto(pos4)
    turtle.goto(pos2)
    turtle.goto(pos5)
    turtle.end_fill()



def main():
    turtle.speed(12)
    turtle.penup()
    x,y=-270,-180
    width,height=540,360
    draw_rectangle(x,y,width,height)
    '''绘制大星'''
    pice = 22
    center_x, center_y = x + 5 * pice ,y + height - 5 * pice
    turtle.goto(center_x,center_y)
    turtle.left(90)
    turtle.forward(3 * pice)
    turtle.right(90)
    draw_star(turtle.xcor(),turtle.ycor(),3 * pice)
    # 画小星星
    x_poses, y_poses = [10, 12, 12, 10], [2, 4, 7, 9]
    for x_pos, y_pos in zip(x_poses, y_poses):
        turtle.goto(x + x_pos * pice, y + height - y_pos * pice)
        turtle.left(turtle.towards(center_x, center_y) - turtle.heading())
        turtle.forward(pice)
        turtle.right(90)
        draw_star(turtle.xcor(), turtle.ycor(), pice)

    # 隐藏海龟
    turtle.ht()
    turtle.mainloop()

if __name__ == '__main__':
    main()    


