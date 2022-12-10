secureFile = None
inStr, secur = "",""
secureFile = open("/Users/imin-ug/Python/PythonGame/난생처음 파이썬/secure.txt","w",encoding = "UTF-8")

while True:
    inStr = input("스파이에게 전달할 메시지 ===> ")
    if inStr =="" :
        break
    for ch in inStr:
        num = ord(ch)
        num += 100
        secur += chr(num)
        
secureFile.writelines(secur)
secureFile.close()
print('---secure.txt 암호화 완료 ----')