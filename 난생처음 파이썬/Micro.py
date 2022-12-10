
Date = int(input("시간을 입력해주세요 =>"))
Date1 = int(input("분을 입력해주세요 =>"))



Time = int(input("조리시간을 입력해주세요. =>"))

if Time <= 0 and Time <= 1000:
    print("{}".format(Time))
    
if (Date>=0 and Date<24) or (Date1>60 and Date1<=0):
    print("현재 시간은 {}시 {}분입니다.".format(Date,Date1))
    Date1 =Time+Date1
    
    if Date1>=60:
        count = int(Date1 /60)
        Date = Date +count
        count1 = int(Date1%60)
        
    else:
        count=0
        count1=0
        
if Date >=24:
    Date = 0
           
print("남은 시간은 {}시 {}분입니다.".format(Date,count1))