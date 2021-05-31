
from selenium import webdriver
import time

#打开谷歌
driver = webdriver.Chrome()

#窗口最大化
driver.maximize_window()

#打开网址
driver.get(r"E:/python自动化技术/python/dbwebday01/资料/练习的html/练习的html/弹框的验证/dialogs.html")

#点击按钮
driver.find_element_by_id("alert").click()

#点击确定
driver.switch_to.alert.accept()
time.sleep(5)
#再点个按钮
driver.find_element_by_id("confirm").click()

#点击取消
driver.switch_to.alert.dismiss()
time.sleep(5)
#关闭网页
driver.quit()










