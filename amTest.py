
import unittest
from Bank import  Bank
from User import  User
from  Address import  Address
class TestBank(unittest.TestCase):
    u=None
    a=None
    b=None
    def setUp(self) -> None:
        self.u=User()
        self.a=Address()
        self.b=Bank()
    def testAddMoney(self):
        #准备数据
        self.u.setAccount("123123")
        self.b.setMoney("100000")
        #期望结果
        staus=1
        #调用方法
        sats=  self.b.bank_addMoney(self.u.getAccount(),self.b.getMoney())
        #自动比较
        self.assertEqual(sats,staus)





















