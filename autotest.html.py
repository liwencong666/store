



from selenium import webdriver
import time

#打开谷歌
driver = webdriver.Chrome()

#打开网址
driver.get(r"E:/python自动化技术/python/dbwebday01/资料/练习的html/练习的html/上传文件和下拉列表/autotest.html")

#窗口最大化
driver.maximize_window()


#输入input的内容
driver.find_element_by_xpath("//*[@name='account']").send_keys("大哥")
driver.find_element_by_xpath("//*[@name='password']").send_keys("二弟")

#下拉列表
driver.find_element_by_xpath("//*[@class='u17']").send_keys("北京市")

#选择性别
driver.find_element_by_xpath("//*[@name='u2' and @id='sexID2']").click()

#选择季节
driver.find_element_by_xpath("//*[@name='u3' and @type='checkbox' and @value='summer']").click()

#上传文件
driver.find_element_by_xpath("//*[@name='file' and @type='file']").send_keys(r"E:\python自动化技术\python\day10\代码\day10\呸.jpg")

#点submit
driver.find_element_by_xpath("//*[@class='u16']").click()

#弹窗点击确定
driver.switch_to.alert.accept()

#睡觉
time.sleep(5)

#关闭
driver.quit()













































































