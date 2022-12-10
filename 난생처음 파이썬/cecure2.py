secureFile = None
inStr, decode = "",""
secureFile = open("/Users/imin-ug/Python/PythonGame/난생처음 파이썬/secure.txt","r",encoding = "UTF-8")


inStr = secureFile.readline()

for ch in inStr:
    num = ord(ch)
    num -= 100   
    decode += chr(num)
        
secureFile.close()
print('---secure.txt 복호화 완료 ----',decode)