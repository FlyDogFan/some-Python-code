import random
num = random.randrange(1,200,2)
print num
num2 = raw_input("������һ������")
if(num2.isdigit()):
    print num*int(num2)
else:
    print "������Ĳ�������"
"""
try:
    num = 1/0
#except:
    #print "��ĸ����Ϊ0"
except ZeroDivisionError:
    print "��ĸ����Ϊ0"
    print ZeroDivisionError
else:
    print "����������"
try:
    num3 = 1/1
finally:
    print "in finally now"
"""
try:
    raise ZeroDivisionError
except ZeroDivisionError:
    print "raise����ĸ����Ϊ0"
username = "admin"
password = "admin"
assert username = "admin" and password = "NOTadmin",'�������'