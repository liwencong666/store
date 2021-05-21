
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
    def testAddress(self):
        #准备数据
        self.u.setAccount("123123")
        self.u.setPassword("123456")
        self.b.setMoney("10000")
        #期望结果
        staus=0
        #调用方法
        sats=  self.b.bank_withdrawal(self.u.getAccount(),self.u.getPassword(),self.b.getMoney())
        #自动比较
        self.assertEqual(sats,staus)





















