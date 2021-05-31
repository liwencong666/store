


from selenium import webdriver
import time

#打开谷歌
driver = webdriver.Chrome()

#打开网址
driver.get(r"E:/python自动化技术/python/dbwebday01/资料/练习的html/练习的html/跳转页面/pop.html")

#窗口最大化
driver.maximize_window()


#输入input的内容
driver.find_element_by_id("goo").click()

#睡觉
time.sleep(5)

#关闭
driver.quit()
















































