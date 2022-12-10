import turtle, random
colorList = ["red", "green", "blue", "black", "magenta", "orange", "gray"]
turtle. shape('turtle')
turtle. setup(550, 550)
turtle.screensize(500, 500) 
turtle.pensize(5)
turtleFile = open("/Users/imin-ug/Python/PythonGame/trace.txt", "w") 
for i in range(30) :
    x = random.randint (-250, 250)
    y = random.randint (-250, 250)
    color = random.choice(colorList)
    turtle.pencolor(color)
    turtle.goto(x,y)
    outStr = str(x) + " " + str(y) + " " + color + "\n"
    turtleFile.writelines(outStr) #파일 저장
turtleFile.close()
turtle.reset()
turtle.pensize(5)
turtleFile = open("/Users/imin-ug/Python/PythonGame/trace.txt","r")
while True :
    inStr = turtleFile.readline()
    if inStr == "":
        break
    x,y,color =inStr.split()
    turtle.pencolor(color)
    turtle.goto(int(x),int(y))
turtleFile.close()