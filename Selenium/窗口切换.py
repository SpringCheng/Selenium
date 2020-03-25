"""
窗口切换
句柄切换

@date: 2020/3/25 16:42 
@author：Spring
"""

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.find_element_by_id('kw').send_keys("柠檬班")
driver.find_element_by_id('su').click()

# 显示等待  等待满足某个条件后去执行下一个操作
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'吧_百度贴吧')]")))





# 切换二
# 窗口切换
# step1:获取窗口的总数及句柄
# handles是一个列表 ，新打开的窗口位于最后
handles = driver.window_handles
print(handles)
time.sleep(1)

# 操作，引起了窗口数量的变化
driver.find_element_by_xpath("//a[contains(text(),'吧_百度贴吧')]").click()
time.sleep(0.5)

# 等待新的窗口出现
WebDriverWait(driver,3).until(EC.new_window_is_opened(handles))

# 重新获取handles
handles = driver.window_handles

# 切换最新打开的窗口
driver.switch_to.window(handles[-1])

# 切换窗口 虽然页面显示是在这个窗口，但是还是要切换窗口后进行点击的
# driver.switch_to.window(handles[-1])
# 等待出现
WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.ID, 'j_head_focus_btn')))
# 点击
driver.find_element_by_id('j_head_focus_btn').click()

# 获取当前的句柄
print(driver.current_window_handle)


#
# EC.new_window_is_opened()
