name="root"
password="admin"
count=1
while True:
    if count <= 3:
       count = count + 1
       name = input("请输入用户名")
       password = input("请输入密码")
       if name == "root" and password == "admin":
        print("登录成功")
       elif name == "root" and password !="admin":
        print("密码错误，登录失败")
       elif name != "root" and password =="admin":
        print("用户名不存在，登录失败")
       else:
        print("登录失败")
    else:
        print("用户锁定")
        break