import random   #随机取数
users = {}
bank_name = "中国工商银行昌平支行"        #银行名称
def welcome():
    print("************************************")
    print("*           中国工商银行             *")
    print("*           账户管理系统             *")
    print("*            V1.0                  *")
    print("* 1.开户                            *")
    print("* 2.存钱                            *")
    print("* 3.取钱                            *")
    print("* 4.转账                            *")
    print("* 5.查询                            *")
    print("* 6.BYE!                           *")
    print("************************************")   #打开欢迎页面

def bank_addUser(account,username,password,country,province,street,door):  #银行的开户逻辑
    if len(users)>=100:
        return 3            #判断字典是否已满
    if account in users:
        return  2           #判断是否存在
    users[account]={
        "username":username,
        "password":password,
        "country":country,
        "province":province,
        "street":street,
        "door":door,
        "money":0,
        "bank_name":bank_name
    }                               #正常开户
    return 1


def addUsers():                 #用户开户方法
    li=["0","1","2","3","4","5","6","7","8","9","a","b","c","d",
        "e","f","g","h","i","j","k","l","m","n","o","p","q","r",
        "s","t","u","v","w","x","y","z"]        #随机获取账号
    account = ""
    for i in range(8):
        index = random.randint(0,len(li)-1)
        account = account + li[index]
        name = input("请输入用户名：")
        password = input("请输入密码：")
        print("请输入您的地址信息：")
        country = input("\t输入国家：")
        province = input("\t输入省份：")
        street = input("\t输入街道：")
        door = input("\t输入门牌号：")            #余额不允许第一次输入
        status = bank_addUser(account,name,password,country,province,street,door)
        if status == 1:
            print("开户成功")
            info ='''
                ---------------个人信息---------------
                账户：%s
                用户名：%s
                取款密码：%s
                地址信息：
                    国家：%s
                    省份：%s
                    街道：%s
                    门牌号：%s
                余额：%s
                开户行：%s
                -------------------------------------
            '''
            print(info % (account,name,password,country,province,street,door,users[account]["money"],bank_name))
        elif status == 2:
            print("对不起，用户已存在，请重新输入")
        elif status == 3:
            print("对不起，银行库已满，请去其他行办理")



def bank_savemoney(account,money):           #存钱
    if account in users:
        users[account]["money"]=users[account]["money"]+money
        return True
    else:
        return False


def bank_drawmoney(account,password,money):          #取钱
    if account not in users:
        return 1
    if password != users[account]["password"]:
        return 2
    if money>users[account]["money"]:
        return  3
    users[account]["money"]=users[account]["money"]-money
    return 0

def bank_transfermoney(account,account1,password,money):        #转账
    if account not in users or account1 not in users:
        return 1
    if password != users[account]["password"]:
        return 2
    if money>users[account]["money"]:
        return 3
    users[account]["money"]=users[account]["money"]-money
    users[account1]["money"]=users[account1]["money"]+money
    return  0

def bank_query(account,password):           #查询
    if account not in users:
        print("该用户不存在")
    if password != users[account]["password"]:
        print("密码不正确")

    print("查询成功")
    info = '''
                    ---------------个人信息---------------
                    账户：%s
                    用户名：%s
                    取款密码：%s
                    地址信息：
                        国家：%s
                        省份：%s
                        街道：%s
                        门牌号：%s
                    余额：%s
                    开户行：%s
                    -------------------------------------
                '''
    print(info % (account, users[account]["name"],users[account]["password"],
                  users[account]["country, province, street, door"], users[account]["money"], bank_name))

def savemoney():            #存钱
    account = input("请输入您的账户：")
    money = input("请输入您的存款金额：")
    money=int(money)
    sta = users[account]["money"]
    if sta == True:
        print("存款成功")
    elif sta == False:
        print("存款失败")

def drawmoney():            #取钱
    account = input("请输入您的账户：")
    password = input("请输入您的密码：")
    money = input("请输入您的取款金额：")
    money = int(money)
    password = int(password)
    sta = bank_drawmoney(account,password,money)
    if sta == 0:
        print("取款成功")
    if sta == 1:
        print("账户不存在")
    if sta == 2:
        print("密码不正确")
    if sta == 3:
        print("余额不足")

def transfermoney():            #转账
    account = input("请输入您的账户：")
    account1 = input("请输入对方账户：")
    password = input("请输入您的密码：")
    money = input("请输入您要转账的金额：")
    password = int(password)
    money = int(money)
    sta = bank_transfermoney(account,account1,password,money)
    if sta == 0:
        print("转账成功")
    if sta == 1:
        print("账户不正确")
    if sta == 2:
        print("密码不正确")
    if sta == 3:
        print("对不起，您账户余额不足")


def query():
    account = input("请输入您的账户")
    password = input("请输入您的密码")
    password = int(password)
    bank_query(account, password)




while True:
    welcome()
    num = input("请输入您的业务编号：")
    if num.isdigit():
        num  = int(num)
        if num == 1:
            addUsers()
        elif num == 2:
            pass
        elif num == 3:
            pass
        elif num == 4:
            pass
        elif num == 5:
            pass
        elif num == 6:
            print("欢迎下次光临")
            break
        else:
            print("输入非法，请重新输入")
    else:
        print("输入非法，请重新输入")





































