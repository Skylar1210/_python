import turtle
import time
import os
def  draw_square(b_x, b_y, x, y):
    turtle.setpos(b_x, b_y)
    turtle.color('red')
    turtle.begin_fill()
    turtle.fd(x)
    turtle.lt(90)
    turtle.fd(y)
    turtle.lt(90)
    turtle.fd(x)
    turtle.lt(90)
    turtle.fd(y)
    turtle.end_fill()
 
def draw_star(s_x, s_y, radius):
    turtle.setpos(s_x, s_y)
    pt1 = turtle.pos()
    turtle.circle(-radius, 72)
    pt2 = turtle.pos()
    turtle.circle(-radius, 72)
    pt3 = turtle.pos()
    turtle.circle(-radius, 72)
    pt4 = turtle.pos()
    turtle.circle(-radius, 72)
    turtle.color('yellow')
    turtle.begin_fill()
    turtle.goto(pt3)
    turtle.goto(pt1)
    turtle.goto(pt4)
    turtle.goto(pt2)
    turtle.end_fill()

#backgroud 
turtle.pu()
draw_square(-320, -240, 660, 440)
ss_x = -320
ss_y = -240 + 440
ss_s = 660 / 30
s_x, s_y = ss_x + ss_s * 5, ss_y - ss_s * 5
turtle.setpos(s_x, s_y)
#big star 
turtle.lt(90)
draw_star(ss_x + ss_s * 5, ss_y - ss_s * 2, ss_s * 3)
 
#small star1
turtle.goto(ss_x + ss_s * 10, ss_y - ss_s * 2)   
turtle.lt(round(turtle.towards(s_x, s_y)) - turtle.heading())
turtle.fd(ss_s)
turtle.rt(90)
draw_star(turtle.xcor(), turtle.ycor(), ss_s)
 
#small star2
turtle.goto(ss_x + ss_s * 12, ss_y - ss_s * 4)    
turtle.lt(round(turtle.towards(s_x, s_y)) - turtle.heading())
turtle.fd(ss_s)
turtle.rt(90)
draw_star(turtle.xcor(), turtle.ycor(), ss_s)
 
#small star3
turtle.goto(ss_x + ss_s * 12, ss_y - ss_s * 7)    
turtle.lt(round(turtle.towards(s_x, s_y)) - turtle.heading())
turtle.fd(ss_s)
turtle.rt(90)
draw_star(turtle.xcor(), turtle.ycor(), ss_s)
 
#small star4
turtle.goto(ss_x + ss_s * 10, ss_y - ss_s * 9)   
turtle.lt(round(turtle.towards(s_x, s_y)) - turtle.heading())
turtle.fd(ss_s)
turtle.rt(90)
draw_star(turtle.xcor(), turtle.ycor(), ss_s)
turtle.ht()
time.sleep(5)
os._exit(1)
