#The rainbow benzene
import turtle
k=turtle.Screen()
color=['red','blue','green','pink','yellow','violet','brown','purple','orange']
t=turtle.Pen()
t.speed(10)
k.bgcolor('black')
k.title("Akash's Benzene")
for x in range(200):
         t.pencolor(color[x%6])
         t.width((x/100)+1)
         t.forward(x)
         t.left(59)
