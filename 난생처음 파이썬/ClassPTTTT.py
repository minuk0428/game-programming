class Car :
    
     def __init__(self,color,speed) :
         self.color = color
         self.speed = speed

     def __str__(self):
         return f'차량1의 섹상은 {self.color}이고, 속도는 {self.speed}입니다.'
    
     def upSpeed(self, x) :
         self.speed += x
     def downSpeed(self, y) :
         self.speed -= y




Car1 = Car(color = "구자민", speed = 10)

print(Car1)

# myDic = {"이름": "이민욱","전화번호":"010-6767-1643"}
# print(myDic)
# myDic["학번"] = "201832036"

# print(myDic.items())
# print(myDic.values())
# print(myDic.keys())

# singer = {}
# singer["태양"] = "눈 코 입"
# singer["김연규"] = "개병신"
# singer["구자민"] = "바보"
# print(singer)
# print(type(singer))
# a =list(singer.items())
# print(type(a[0]))
# for k in singer:
#     print(k,"==>",singer[k],end='')