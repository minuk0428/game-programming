from email.mime import image
import pygame
import PIL 
import random as r
import turtle as t

from PIL import Image

colorList = ["red", "blue", "black" , "magenta","orange","gray"]
t.shape('turtle')
t.setup(850, 850)
t.screensize(800, 800)
t.speed(0)
t.penup()

for num in range(1, 37, 1):
    t.goto(0,0)
    t.right(10)
    t.forward(350)
    t.pencolor(r.choice(colorList))
    t.write(str(num), font=('맑은고딕', 20, 'bold'))
    
t.goto(0,0)
t.pendown()
t.pensize(5)

angle = r.randint(10,360) //10 * 10
t.right(angle)
t.forward(350)

number = angle // 10
if number < 10:
    number = '0' + str(number)
else :
    number = str(number)

filename = "/Users/imin-ug/Python/PythonGame/OneDrive_2022-10-13/photo/picture"+number+".jpg"
img = Image.open(filename)
img.show()