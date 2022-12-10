# fact = 1
# for i in range(1,6,1):
#     fact = fact * i

# print(fact)
# a = 0
# for i in range(1,11):
#     a= a+i
#     print(a)


# for i in range(1,10):
#     for k in range(1,10):
#         print("{} X {} = {}".format(i,k,i*k))
# i= 0
# while i<5:
#     i = i+1
#     print(i)
'''
다시 풀어보기
import random as r


i = 0
while True:
    dice1 = r.randint(1,6)
    dice2 = r.randint(1,6)
    dice3 = r.randint(1,6)
    if dice1 == dice2 == dice3:
        print("{} {} {}  {}번 반복했음".format(dice1,dice2,dice3,i))
    else:
        print(i,"번째 반복") 
    i += 1'''
# import random as r

# b = r.randint(1,5)

# while True:

#     a = int(input("수를 입력하세요 ==> "))
#     if a == b:
#         print("맞췄습니다. ")
#     else:
#         print("틀렸습니다. ")

import turtle as t
import random as r
t.shape("turtle")
colors = ["red","blue" ,"green", "magenta", "black"]
t.penup()
t.screensize(300,300)
t.setup(330,330)

for i in range(7):
    for k in range(7):
        x = k*50-150
        y = i*50-150
        t.goto(x,y)
        t.color(r.choice(colors))
        t.stamp()
t.done