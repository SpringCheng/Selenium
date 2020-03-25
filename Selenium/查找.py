"""

@date: 2020/3/24 16:49 
@author：Spring
"""

from selenium import webdriver
import time

driver = webdriver.Chrome(service_log_path='D:\Practice\Log\chromedriver.log')
driver.get("http://www.baidu.com")

# 窗口最大化
driver.maximize_window()

driver.find_element_by_id('kw').send_keys("python")
driver.find_element_by_id("su").click()
time.sleep(3)

driver.get("https://taobao.com")
# 回退上一页
time.sleep(2)
driver.back()

# 回到下一页(前进）
time.sleep(2)
driver.forward()

# 刷新
time.sleep(2)
driver.refresh()

# 获取标题
print(driver.title)

# 获取网址
print(driver.current_url)

# 获取窗口的句柄  浏览器窗口的属性用句柄（handle）来识别
print(driver.current_window_handle)

# 退出
# driver.quit()
