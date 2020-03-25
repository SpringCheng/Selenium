"""
自己练手的
@date: 2020/3/25 21:47 
@author：Spring
"""

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# import time

driver = webdriver.Chrome()
driver.get('https://wwww.baidu.com')

# 1、定位元素来输入搜索
driver.find_element_by_id('kw').send_keys('柠檬班')

# 2、点击“百度”按钮
driver.find_element_by_id('su').click()

# 3、等待搜索结果加载完（显示等待）
# 等待通过By.ID找到的可见元素加载完
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'吧_百度贴吧')]")))

# 4、点击操作之前的窗口数（获取当前所有的当前打开窗口句柄）
# 这个窗口总数应该是在未生成新窗口的时候来判断
handles = driver.window_handles

# 5、操作，引起窗口数量的变化(点击链接生成一个新窗口)
driver.find_element_by_xpath("//a[contains(text(),'吧_百度贴吧')]").click()

# 6、等待新窗口的加载完
# EC.new_window_is_opened()判定新的窗口是否打开：传入当前的窗口总数来和传进来的窗口总数比大小，来判断你是否有新的窗口打开
WebDriverWait(driver,3).until(EC.new_window_is_opened(handles))

# 7、获取新的当前的窗口总数
handles = driver.window_handles

# 8、切换到当前的新窗口
driver.switch_to.window(handles[-1])

# 9、等待出现
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'j_head_focus_btn')))

# 10、点击
driver.find_element_by_id('j_head_focus_btn').click()


