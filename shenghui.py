
names=["北京","上海","广东","哈尔滨","长春","沈阳","呼和浩特","石家庄","乌鲁木齐","兰州","西宁","西安","银川",
       "郑州","济南","太原","合肥","武汉","长沙","南京","成都","贵阳","昆明","南宁","拉萨",
       "杭州","南昌","广州","福州","台北","海口"]
names.remove("广东")
names.insert(1,"广东")
print(names)



li=[36710.36,35427.10,29863.23,29667.39,27665.36,27650.45,27620.38,25369.20]
print(li[0]+li[1]+li[2]+li[3]+li[4]+li[5]+li[6]+li[7])
print((li[0]+li[1]+li[2]+li[3]+li[4]+li[5]+li[6]+li[7])/8)

a = [1,5,21,30,15,9,30,24]
b = len(a)
c = 0    #循环次数
d = 0     #求和
while c<b:
    if (a[c])%5 == 0:
        d=d+a[c]
        c=c+1
    elif a[c]%5 != 0:
        c = c+1
print(d)




listnode = [1,2,3,4,5,6,7,8,9]
newList = list(reversed(listnode))
print(newList)

li = [1,4,7,5,8,2,1,3,4,5,9,7,6,1,10]
a=0     #列表位置
b=0     #次数
while True:
    num=input("请输入数字")
    num=int(num)
    if num==li[a]:
        b=b+1
        a=a+1
    elif num!=li[a]:
        a=a+1
    print(b)













