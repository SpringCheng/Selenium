"""
# 鼠标操作
ActionChains(driver).move_to_element(ele).perform()
ActinChains类的实例化
    drag_and_drop
    context_click
    double_click
鼠标移动上去的下拉列表操作
@date: 2020/3/26 15:29 
@author：Spring
"""

from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.maximize_window()

# 1、先找到要操作的元素位置
ele = driver.find_element_by_xpath("//*[@id='u1']//a[@name='tj_settingicon']")

# # (2)、实例Actionchains类
# action = ActionChains(driver)
#
# # (3)、将鼠标操作存储在action列表中
# ac.move_to_element(ele)
#
# # (4)、调用perform（）来执行鼠标操作
# action.perform()

# 2、(2)(3)(4)步合成一步写   鼠标移到某一个元素上，弹出下拉列表
ActionChains(driver).move_to_element(ele).perform()

# 3、选择下拉列表中的“高级搜索”点击

# 方式一:根据文本内容定位 contains(text())
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//a[text()="高级搜索"]')))
driver.find_element_by_xpath('//a[text()="高级搜索"]').click()

# 方式二：下拉列表使用for循环定位


