# class Car :
   
#    def __init__(self,색상,현재속도):
#         self.색상 = 색상
#         self.현재속도 = 현재속도
#    def upSpeed(self):      
#        self.현재속도+=30
#        return self.현재속도

# for i in range(0,3):
#     car1 = Car("빨강",30)
#     car1.upSpeed()
# print(car1.색상, car1.현재속도)

class length_line :
    def __init__(self,length):
        self.length = length
        print("길이가 생성됐습니다.")
        
    def __add__(self,other):
        return self.length + other.length
    
    def __lt__(self,other):
        return self.length < other.length
    
    def __eq__(self,other):
        return self.length == other.length
    
a = length_line(5)
b = length_line(10)

print("두 선의 길이의 합 ",a==b)


