class BreadMold:
    category = "빵"
    
    def __init__(self,category, price):
        self.category = category
        self.price = price
        print("빵을 만들었습니다. ")
        
    def __del__(self):
        print("빵이 없습니다.")
     
 
 #_init_ 생성자 메서드    
bread1 = BreadMold("붕어빵",3000)
bread2 = BreadMold("잉어빵",4000)
print("{}의 가격은 {}원 입니다.".format(bread1.category,bread1.price))
print("{}의 가격은 {}원 입니다.".format(bread2.category,bread2.price))

# bread1.price = 3000
# bread2.category = "붕어빵"
# bread3.category = "잉어빵"

# print(bread1.category,bread2.category,bread3.category)

# #dir() 이름 공간에 있는 모든 속성을 리스트로 반환

# print(dir(bread1))

# print(dir(BreadMold))

