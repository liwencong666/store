from threading import Thread
import time

basket = 0   #篮子
seconds = 0     #时间

class Shi(Thread):
    def run(self) -> None:
        global seconds
        while True:
            if seconds <= 300:
                time.sleep(1)
                seconds = seconds + 1
                print("现在已过",seconds,"秒了，要买面包的抓紧了")
            else:
                break

class Cooker(Thread):
    username = ""
    count = 0       #每个厨师做出的面包数

    def run(self) -> None:
        global basket
        while True:
            if basket >= 300:
                time.sleep(60)
                print("对不起，篮子已满，不能再放面包了")
                print(self.username,"做了",self.count,"个面包")
            else:
                basket = basket + 1
                self.count = self.count + 1
                print("恭喜",self.username,"做出一个面包,篮子里还剩",basket,"个面包")

class Customer(Thread):
    name = ""
    number = 0
    def run(self) -> None:
        global basket
        while True:
            if basket <= 0:
                time.sleep(60)
                print("对不起，篮子空了，不能买了")
                print(self.name,"买了",self.number,"个面包")
            else:
                basket = basket - 1
                self.number = self.number + 1
                print("恭喜",self.name,"买到一个面包，篮子里还剩",basket,"个面包","花了",self.number*10,"元")

C1 = Cooker()
C2 = Cooker()
C3 = Cooker()
C4 = Cooker()
C5 = Cooker()
C6 = Cooker()

C1.username = "赵一"
C2.username = "钱二"
C3.username = "孙三"
C4.username = "李四"
C5.username = "王五"
C6.username = "韩老六"
D1 = Customer()
D2 = Customer()
D3 = Customer()
D4 = Customer()
D5 = Customer()

D1.name = "包拯"
D2.name = "张龙"
D3.name = "赵虎"
D4.name = "王朝"
D5.name = "马汉"

C1.start()
C2.start()
C3.start()
C4.start()
D1.start()
D2.start()
D3.start()
D4.start()
D5.start()

C5.start()
C6.start()

#
# class Person(Thread):
#     username = ""
#     count  = 0
#
#     def run(self) -> None:
#         global  tiket  # 将tiket 申明为全局变量，在方法里进行使用
#         while True:
#             if tiket <= 0:
#
#                 print("对不起，",self.username,"没有抢到票了！")
#                 print(self.username,"本次抢了",self.count,"张票！")
#                 break
#             else:
#
#                 tiket = tiket - 1
#                 self.count = self.count + 1
#                 print("恭喜",self.username,"抢到 1 张票，还剩",tiket,"张票！")
#                 time.sleep(2)
#
# p1 = Person()
# p2 = Person()
# p3 = Person()
#
# p1.username = "张家辉"
# p2.username = "杜旱情"
# p3.username = "旺财"






































