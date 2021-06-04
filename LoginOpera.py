
class LoginPage:
    def __init__(self,driver):
        self.driver = driver

    #封装登录逻辑
    def login(self,username,password):
        #输入用户名
        self.driver.find_element_by_id("loginname").send_keys(username)
        #输入密码
        self.driver.find_element_by_id("password").send_keys(password)
        #点击登录
        self.driver.find_element_by_id("submit").click()

    #获取登录成功的实际结果
    def get_success_login(self):
        return self.driver.title
    # #获取密码错误情况下的登录失败的实际结果
    # def get_error_password_login(self):
    #     return self.driver.find_element_by_id("msg_uname").text
    # #获取账户错误情况下登录失败的实际结果
    # def get_error_username_login(self):
    #     return self.driver.find_element_by_id("loginname").text
    # #获取账户密码都错误的情况下登录失败的实际结果
    # def get_error_quanbu_login(self):
    #     return self.driver.find_element_by_id("msg_uname").text
    #
