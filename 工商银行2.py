import random
from DBUtils import update
from DBUtils import select

bank_name = "中国工商银行昌平支行"


def welcome():
    print("---------------------------------")
    print("-     中国工商银行账户管理系统V1.0     -")
    print("---------------------------------")
    print("-   1.开户                       -")
    print("-   2.存钱                       -")
    print("-   3.取钱                       -")
    print("-   4.转账                       -")
    print("-   5.查询                       -")
    print("-   6.Bye!                       -")
    print("----------------------------------")


# 银行的开户逻辑
def bank_addUser(account,username,password,country,province,street,door):
    # 判断是否已满
    sql = "select count(*) from users"

    data = select(sql,[]) # ((72),(),())
    print(data)
    if data[0][0] >= 100:
        return 3
    # 判断是否存在
    sql1 = "select * from users where account = %s"
    data1 = select(sql1,account) #(("张三"),(“李四”))
    if len(data1) != 0:
        return 2
    #正常开户
    # 数据存到数据库里
    sql2 = "insert into users values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    param2 = [account,username,password,country,province,street,door,bank_name,0]
    update(sql2,param2)
    return 1


# 用户开户方法
def addUser():
    # 随机获取账号
    li = ["1","2","3","4","5","6","7","8","9","0","a","b","c","e","f"]
    account = ""
    for i in range(8):
        index = random.randint(0, len(li) - 1)
        account = account + li[index]
    name = input("请输入用户名：")
    password = input("请输入您的密码（6位数字）：")
    print("接下来要输入您的地址信息：")
    country = input("\t输入国家：")
    province = input("\t输入省份：")
    street =  input("\t输入街道：")
    door = input("\t输入门牌号：")
    # 余额不允许第一次输入，需要存钱

    status = bank_addUser(account,name,password,country,province,street,door)
    if status == 1:
        print("恭喜开户成功！")
        info = '''
            ------------个人信息----------------
            账号：%s,
            用户名：%s,
            取款密码：%s,
            地址信息：
                国家：%s,
                省份：%s,
                街道：%s,
                门牌号：%s,
            余额：%s,
            开户行：%s
            -----------------------------------
        '''
        print(info % (account,name,password,country,province,street,door,0,bank_name))

    elif status == 2:
        print("对不起，该用户已存在！请稍后重试！！！")
    elif status == 3:
        print("对不起，该银行库已满，请携带证件到其他银行办理！！！")



#   银行的存钱方法
def bank_saveMoney(account,money):
    #判断是否存在
    sql = "select * from users where account = %s"
    param = [account]
    data = select(sql,param)
    if len(data) != 0:
        sql1 = "update users set money = money+%s where account = %s"
        param1 = [money,account]
        update(sql1,param1)
        return True
    return False

#   银行的取钱方法
def bank_takeMoney(account,password,money):
    #判断是否存在
    sql = "select * from users where account = %s"
    param = [account]
    data = select(sql,param)
    if len(data) == 0 :
         return 1

    
    sql1 = "select password from users where account = %s"
    data = select(sql1,param)
    if data[0][0] !=password:
        return 2

    sql2 = "select money from users where account = %s"
    data = select(sql2,param)
    if data[0][0] !=money:
        return 3

    sql3 = "update users set money=money-%s where account = %S"
    param3 = [money,account]
    update(sql3,param3)
    return 0



#   银行的转账功能
def bank_transformMoney(outputaccount,inputaccount,outputpassword,outputmoney):
    sql = "select account from users where account = %s"
    sql1 = "select account from users where account = %s"
    param = [outputaccount]
    param1 = [inputaccount]
    data = select(sql,param)
    data1 = select(sql1,param1)

    if len(data) == 0 and len(data1) ==0:
        return 1

    sql2 = "select outputpassword from users where account = %s"
    param2 = [outputaccount]
    data2 = select(sql2,param2)
    if data2[0][0] != outputpassword:
        return 2

    sql3 = "select outputmoney from users where account = %s"
    param3 = [outputaccount]
    data3 = select(sql3,param3)
    if data3[0][0]<outputmoney:
        return 3

    sql4 = "updata users set money=money-%s where account = %s"
    param4 = [outputmoney,outputaccount]
    update(sql4,param4)
    sql5 = "updata users set money=money+%s where account = %s"
    param5 = [outputmoney,inputaccount]
    update(sql5,param5)
    return 0


#   银行的查询功能

def bank_selectUser(account,password):
    sql = "select * from users where account = %s"
    param = [account]
    data = select(sql,param)
    if len(data) != 0:
        sql1 = "select * from users where account = %s"
        param1 = [account]
        data1 = select(sql1,param1)
        if data1[0][2]==password:
            print("查询成功")
            sql2 = "select * from users where account = %s"
            param2 = [account]
            data2 = select(sql2,param2)
            print(data2)
            info = '''
                       -----------个人账户信息------------
                       账户：%s，
                       用户名：%s，
                       取款密码：%s ，
                       地址信息：
                             国家：%s，
                             省份：%s，
                             街道：%s ，
                             门牌号：%s，
                       余额：%s ，
                       开户行：%s
                       ---------------------------------
            '''
            print(info % (data1[0][0],data1[0][1],data1[0][2],data1[0][3],data1[0][4],data1[0][5],data1[0][6],data1[0][7],data1[0][8],))

        else:
            print("密码错误")
    else:
        print("用户不存在")

# 存钱
def saveMoney():
    account = input("请输入账号")
    money = input("存入的金额")
    money = int(money)
    sta = bank_saveMoney(money,account)
    if sta == True:
        print("成功存入",money,"元")
    elif sta == False:
        print("对不起，该用户不存在")
    else:
        print("对不起，系统出错，请重新操作")

# 取钱
def takeMoney():
    account = input("账户")
    password =  input("密码")
    password = int(password)
    money = input("取出金额")
    money = int(money)

    f = bank_takeMoney(account,password,money)

    if f == 1:
        print("该用户不存在！")
    elif f == 2:
        print("密码错误！")
    elif f == 3:
        print("取款金额不足！")
    elif f == 0:
        print("取款成功！")
        bank_selectUser(account,password)


# 转账功能
def transformMoney():
    outputaccount = input("转出的账号")
    inputaccount = input("转入的账号")
    outputpassword =  input("转出的密码")
    outputpassword = int(outputpassword)
    outputmoney = input("要转出的金额")
    outputmoney = int(outputmoney)

    f = bank_transformMoney(outputaccount,inputaccount,outputpassword,outputmoney)

    if f==0:
        print("转账成功")
    elif f == 1:
        print("转出或转入的账号不存在！")
    elif f == 2:
        print("输入密码错误！")
    elif f == 3:
        print("转账金额不足！")
    else:
        print("转账成功！")
        print("您的个人信息：")
        bank_selectUser(outputaccount,outputpassword)

# 查询账户方法
def selectUser():
    account = input("账号")
    password = input("密码")
    password = int(password)

    bank_selectUser(account,password)


# 核心程序
while True:
    welcome()
    chose = input("选项")

    if chose  == "1":
        addUser()
    elif chose == "2":
            saveMoney()
    elif chose == "3":
            takeMoney()
    elif chose == "4":
            transformMoney()
    elif chose == "5":
            selectUser()
    elif chose == "6":
            print("Bye,Bye您嘞！！！！")
            break
    else:
        print("不存在改选项，别瞎弄！")





