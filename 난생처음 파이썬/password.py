
def checkPassword(pwd):
    if len(pwd) < 8:
        return False
    if pwd.isalnum(): #문자나 숫자로만 이루어져있으면 트루 반환
        return True
    else :
        return False
    
password = ""
password = input("새로운 비밀번호를 입력하세요. ")

if checkPassword(password):
    print("GOOD! 비밀번호가 올바르게 생성되었습니다. ")
else :
    print("오류! 비밀번호가 규칙에 맞지 않습니다.")
