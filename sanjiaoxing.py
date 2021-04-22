a=input("请输入数字")
b=input("请输入数字")
c=input("请输入数字")
a=int(a)
b=int(b)
c=int(c)

if a == b!=c or a == c!=b or b == c!=a and a+b>c and b+c>a and a+c>b:
    print("等腰三角形")
elif a==b==c:
    print("等边三角形")
elif a*a+b*b==c*c or a*a+c*c==b*b or b*b+c*c==a*a:
    print("直角三角形")
elif a+b>c or a+c>b or b+c>a:
 print("直角三角形")
else:
 print ("不能构成三角形")




