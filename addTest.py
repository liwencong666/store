import unittest
from Bank import  Bank
from User import  User
from  Address import  Address
class TestAddress(unittest.TestCase):
    u=None
    a=None
    b=None
    def setUp(self) -> None:
        self.u=User()
        self.a=Address()
        self.b=Bank()
    def testAddress(self):
        #准备数据
        self.u.setAccount("123123")
        self.u.setUsername("jason")
        self.u.setPassword("123456")
        self.a.setCounrry("zg")
        self.a.setProvince("zj")
        self.a.setStreet("bh")
        self.a.setDoor("17")
        #期望结果
        staus=1
        #调用方法
        sats=  self.b.bank_addUser(self.u.getAccount(),self.u.getUsername(),self.u.getPassword(),
                                   self.a.getCounrry(),self.a.getProvicne(),self.a.getStreet(),self.a.getDoor())
        #自动比较
        self.assertEqual(sats,staus)


