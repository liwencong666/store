from selenium import webdriver
import time
from selenium.webdriver import ActionChains

#打开浏览器
driver = webdriver.Chrome()

#窗口最大化
driver.maximize_window()

#打开网址
driver.get("http://www.jd.com")
time.sleep(5)

#点击登录
driver.find_element_by_xpath("//*[@id='ttbar-login']/a[1]").click()
#//*[@id="ttbar-login"]/a[1]
time.sleep(2)
#点击账号登录
driver.find_element_by_xpath("//*[@id='content']/div[2]/div[1]/div/div[3]/a").click()
time.sleep(2)
#输入手机号
driver.find_element_by_xpath("//*[@id='loginname']").send_keys("13008016530")
time.sleep(2)
#输入密码
driver.find_element_by_xpath("//*[@id='nloginpwd']").send_keys("s1075576058")
time.sleep(2)
#点击验证按钮
driver.find_element_by_xpath("//*[@id='loginsubmit']").click()
time.sleep(10)
#输入框中输入内容
driver.find_element_by_xpath("//*[@id='key']").send_keys("充气娃娃")
time.sleep(2)
#点击搜索按钮
driver.find_element_by_xpath("//*[@id='search']/div/div[2]/button/i").click()
time.sleep(5)
#选择店铺
driver.find_element_by_xpath("//*[@id='J_goodsList']/ul/li[1]/div/div[3]/a/em").click()
time.sleep(2)
#窗口切换
a = driver.window_handles
time.sleep(1)
#获取第二个窗口
driver.switch_to.window(a[1])
time.sleep(1)
# #选择商品类型
# driver.find_element_by_xpath("//*[@id='choose-attr-1']/div[2]/div[4]/a").click()
# time.sleep(5)
#添加购物车
driver.find_element_by_xpath("//*[@id='InitCartUrl']").click()
time.sleep(1)
#查看购物车
driver.find_element_by_xpath("//*[@id='settleup-2014']/div[1]").click()
#//*[@id="settleup-2014"]/div[1]
time.sleep(10)
#窗口再次切换
a = driver.window_handles
time.sleep(1)
#获取第三个窗口
driver.switch_to.window(a[2])
time.sleep(1)
#删除购物车商品
driver.find_element_by_xpath("//*[@id='10020371708518']/div[1]/div[7]/a[1]").click()
#//*[@id="10020371708518"]/div[1]/div[7]/a[1]
time.sleep(5)
#确定删除
driver.find_element_by_xpath("/html/body/div[10]/div[1]/div/div/div/p/a[2]").click()
time.sleep(1)
#关闭浏览器
driver.quit()








