


li=[1,12,3,2,4,5,4,3,2,1,2,]
li[2]=45
li.append(33)
print(li)
li.remove(2)
print(li)



import collections
a = [1,2,3,1,2,3,4,1,2,5,4,6,7,7,8,9,6,2,23,4,2,1,5,6,7,8,2]
b = collections.Counter(a)
for c in b:
    print("数字",c,"出现",b[c])









