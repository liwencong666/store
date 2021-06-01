from selenium import webdriver
import time
from selenium.webdriver import ActionChains

#打开浏览器
a = webdriver.Chrome()
time.sleep(1)
#窗口最大化
a.maximize_window()
time.sleep(1)
#打开网页
a.get("http://www.qcc.com")
time.sleep(10)
#定位叉叉
a.find_element_by_xpath("//*[@id='addfavorModal']/div/div/div[1]/img[1]").click()
time.sleep(5)
#点击登录
a.find_element_by_link_text("登录 | 注册").click()
time.sleep(5)
#选中滑块
b = a.find_element_by_xpath("//*[@id='nc_1_n1z']")
time.sleep(5)
#创建action
c = ActionChains(a)
time.sleep(5)
#滑动
c.click_and_hold(b).move_by_offset(348.0).perform()

time.sleep(5)
a.quit()






