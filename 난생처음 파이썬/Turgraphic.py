# import random as r
# import turtle as t

# t.screensize(500,500)
# t.setup(550,550)
# liist = []
# a = ()
# for i in range(0,100):
#     x = r.randint(-250,250)
#     y = r.randint(-250,250)
#     a = (x,y)
#     liist.append(a)
#     print(liist[i])

def adgu(x,y):
    result = x+y
    return result

a = int(input("==>"))
b = int(input("==>"))

print(adgu(a,b))