from selenium import webdriver
from selenium.webdriver import ActionChains
import time


#打开浏览器
w = webdriver.Chrome()
#打开网页
w.get("https://www.baidu.com/")
#窗口最大化
w.maximize_window()
#定位输入框
c=w.find_element_by_xpath("//*[@id='kw']")
ac=ActionChains(w)
c.click()
ac.key_down("a").key_up("a").perform()
time.sleep(6)
w.quit()











