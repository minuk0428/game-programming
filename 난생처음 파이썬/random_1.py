import random
# a = random.randint(1, 45)
# print(a)

# a = input("나이를 입력하시오 => ")

# if a>=19:
#     print("통과")
# elif a<19:
#     print("안됨")

a = random.choice(["가위", "바위", "보"])
print(a)
b = input("가위 바위 보를 입력하세요 ==> ")
# 가위 0 바위 1 보2

while True:
    if a== b:
        print("비겼습니다. ")
    elif b=='가위' and a=='보':
        print("이겼습니다.")
    elif b=='가위' and a=='바위':
        print("졌습니다. ")
    elif b=='바위' and a=='가위':
        print("이겼습니다. ") 
    elif b=='바위' and a=='보':
        print("졌습니다. ")
    elif b=='보' and a=='바위':
        print("이겼습니다. ")
    elif b=='보' and a=='가위':
        print("졌습니다. ")