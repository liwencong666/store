f1=open(file="用户输入",mode="rb")
f2=open(file="D:\python\hAHA.png",mode="wb")
data = f1.read()
f2.write(data)
f2.close()
f1.close()