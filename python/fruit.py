#_*_ coding:utf-8 _*_
def checkfruits(fruit_check):
    checked = ["苹果","香蕉"]
    for i  in fruit_check :
        if i not in checked:
            checked.append(i)
    print "现有水果："
    checked.sort(reverse = True)
    for item in checked:
        print item
    return checked
fruit_list = ["苹果","栗子","李子","香蕉","桃子","西红柿"]
fruit_add = raw_input ("请输入你要添加的水果：")
fruit_list.append(fruit_add)
checkfruits(fruit_list)
fruit_search = raw_input("请输入你要查找的水果：")
try:
    print '你要查找的水果：'+fruit_search+'在第'+str(rank)+'个'
except:
    print '找不到你要查找的水果！'
"""
"""
import re

L = "hellohellohello"
N = "good"
N = "wherewhere"

cnt = 0
result = ''
for i in range(1,len(L)+1):
    if cnt <= len(re.findall(L[0:i],L)):
        cnt = len(re.findall(L[0:i],L))
        result = re.findall(L[0:i],L)[0]

print(result)