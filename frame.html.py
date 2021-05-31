
from selenium import webdriver
import time

#打开谷歌
driver = webdriver.Chrome()

#打开网址
driver.get(r"E:/python自动化技术/python/dbwebday01/资料/练习的html/练习的html/frame.html")

#窗口最大化
driver.maximize_window()

#切换框架
#driver.switch_to.frame("frame")

#输入input的内容
driver.find_element_by_id("input1").send_keys("大哥")

#睡觉
time.sleep(5)

#关闭
driver.quit()






















