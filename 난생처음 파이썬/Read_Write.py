#  open()으로 파일명 지정  읽기는 r를 사용

inFile, outFile = None, None
inStr = ""

inFile = open("/Users/imin-ug/Python/PythonGame/난생처음 파이썬/exam.txt","r",encoding = "UTF-8")
outFile = open("/Users/imin-ug/Python/PythonGame/난생처음 파이썬/note.txt","w")

inList = inFile.readlines()
for inStr in inList:
    outFile.writelines(inStr)
    
inFile.close()
outFile.close()
print("====exam.txt가 note.txt로 복사되었음 ====")