import datetime
import re

# birthdate="21-12-1997"


# num = re.findall(r'\d+', birthdate)

# num = [int(i) for i in num]

 
# print(num)

bdate = "12-03-1997"

def days(birthdate):
    num = re.findall(r'\d+', birthdate)
    num = [int(i) for i in num]
    now = datetime.datetime.now()
    bdate = datetime.datetime(num[2],num[1], num[0])
    difference = now - bdate
    difference = difference.days
    return difference

print(days(bdate))