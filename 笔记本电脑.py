class computer:
    __screen = ""        #屏幕
    __price = 0         #价格
    __model = ""        #cup型号
    __memory = ""       #内存
    __standby = ""      #待机时长

    def setscreen(self,screen):
        self.__screen=screen
    def getscreen(self):
        return self.__screen
    def setprice(self,price):
        self.__price=price
    def getprice(self):
        return self.__price
    def setmodel(self,model):
        self.__model=model
    def getmodel(self):
        return self.__model
    def setmemory(self,memory):
        self.__memory=memory
    def getmemory(self):
        return self.__model
    def setstandby(self,standby):
        self.__standby=standby
    def getstandby(self):
        return  self.__standby
    def typ(self,typscreen):
        print(self.__screen,"在用",typscreen,"的大电脑打字")
    def show(self):
        print("我的电脑是",self.__model,"型号的，电脑屏幕有",self.__screen,"大，内存",self.__memory,
              "超长待机时间",self.__standby,"hour,只花了",self.__price)

c=computer()
c.setscreen("30英寸")
c.setprice(5000)
c.setmodel("xx")
c.setmemory("20T")
c.setstandby("20")

c.show()










