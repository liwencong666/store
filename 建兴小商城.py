
shop = [
    ["康师傅肥牛火锅面",2],
    ["康师傅京都炸酱面",2],
    ["康师傅排骨炖鸡面",2],
    ["辣条",5],
    ["lenovo电脑",5000]
]

import random
X = random.randint(10,31)
print(X)

salary = input("请输入您的余额")
salary = int(salary)
a=salary
mycart = []


while True:
    for index, value in enumerate(shop):
        print(index, "  ", value)
    num = input("请输入你需要的商品")
    if num.isdigit():
        num = int(num)
        if num > len(shop):
           print("商品不存在，请重新选择")
        else:
            if salary >= shop[num][1]:
                mycart.append(shop[num])
                salary=salary-shop[num][1]
                price=a-salary
                integral=price/10
                if price>=600:
                    X>=10 and X<20
                    price=price-300
                elif X>=20:
                    price=price-((shop[4][1])/2)
                print("成功添加到购物车")
            else:
                print("对不起，您的余额不足，请充值")
    elif num == "Q" or num == "q":
        print("欢迎下次光临")
        break
    else:
        print("非法输入，请重新输入")


print("您本次购物商品如下：")
for index,value in enumerate(mycart):
    print(index,"  ",value)
print("您的余额为：",salary)
print("您本次消费：",price)
print("您本次消费累计的积分为：",integral)








