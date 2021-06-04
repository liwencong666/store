from ddt import ddt
from ddt import data

from selenium import  webdriver
import unittest
from InitPage import InitPageData
from LoginOpera import LoginPage
import time
@ddt
class LoginTest(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()


        self.driver.get("http://www.jasonisoft.cn:8080/HKR")
        time.sleep(3)
    def tearDown(self) -> None:
        time.sleep(1)
        self.driver.quit()

    #登录成功测试用例
    @data(*InitPageData.success_data)
    def test_success_login(self,testdata):
        #创建页面操作逻辑对象

        login = LoginPage(self.driver)
        #执行登录逻辑
        login.login(testdata["username"],testdata["password"])
        #获取实际结果
        result = login.get_success_login()
        #把期望结果提取出来
        expect = testdata["expect"]
        #断言
        self.assertEqual(expect,result)

    # #密码错误的情况下登录失败测试用例
    # @data(*InitPageData.password_error_data)
    # def test_error_login(self, testdata):
    #     # 创建页面操作逻辑对象
    #
    #     login = LoginPage(self.driver)
    #     # 执行登录逻辑
    #     login.login(testdata["username"], testdata["password"])
    #     # 获取实际结果
    #     result = login.get_error_password_login()
    #     # 把期望结果提取出来
    #     expect = testdata["expect"]
    #     # 断言
    #     self.assertEqual(expect, result)
    #
    # #账户错误的情况下登录失败的测试用例
    # @data(*InitPageData.username_error_data)
    # def test_error_login(self, testdata):
    #     # 创建页面操作逻辑对象
    #
    #     login = LoginPage(self.driver)
    #     # 执行登录逻辑
    #     login.login(testdata["username"], testdata["password"])
    #     # 获取实际结果
    #     result = login.get_error_username_login()
    #     # 把期望结果提取出来
    #     expect = testdata["expect"]
    #     # 断言
    #     self.assertEqual(expect, result)
    #
    # #账户密码都错误的情况下登录失败的测试用例
    # @data(*InitPageData.quanbu_error_data)
    # def test_error_login(self, testdata):
    #     # 创建页面操作逻辑对象
    #
    #     login = LoginPage(self.driver)
    #     # 执行登录逻辑
    #     login.login(testdata["username"], testdata["password"])
    #     # 获取实际结果
    #     result = login.get_error_quanbu_login()
    #     # 把期望结果提取出来
    #     expect = testdata["expect"]
    #     # 断言
    #     self.assertEqual(expect, result)
    #
    #

