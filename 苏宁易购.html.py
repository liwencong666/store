from selenium import webdriver
import time


#打开浏览器
a=webdriver.Chrome()
#窗口最大化
a.maximize_window()
#打开网页
a.get("http://www.suning.com")
time.sleep(10)

#输入框输入
a.find_element_by_xpath("//*[@id='searchKeywords']").send_keys("充气娃娃")
time.sleep(5)
#点击搜索
a.find_element_by_xpath("//*[@id='searchSubmit']").click()
time.sleep(5)

#点击搜索到的商品
a.find_element_by_xpath("//*[@id='0070145111-12084012802']/div/div/div[2]/div[2]/a").click()

time.sleep(5)
#窗口切换
w = a.window_handles
print(w)
time.sleep(5)
#获取第二个窗口
a.switch_to.window(w[1])
time.sleep(5)

#点击加入购物车
a.find_element_by_xpath("//*[@id='addCart']").click()
time.sleep(5)

#关闭
a.quit()







