class cup:
    __high = 0
    __volume = 0
    __color = ""
    __material = ""

    def sethigh(self,high):
        self.__high=high

    def gethigh(self):
        return self.__high

    def setvolume(self,volume):
        self.__volume=volume

    def getvolume(self):
        return self.__volume

    def setcolor(self,color):
        self.__color=color

    def getcolor(self):
        return  self.__color

    def setmaterial(self,material):
        self.__material=material

    def getmaterial(self):
        return  self.__material

    def show(self):
        print("这个水杯能装",self.__volume,"水")

u = cup()
u.setvolume("2L")
u.show()






















