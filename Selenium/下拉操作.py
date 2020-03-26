"""

@date: 2020/3/26 16:37 
@author：Spring
"""

from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.maximize_window()

# 1、先找到要操作的元素位置
ele = driver.find_element_by_xpath("//*[@id='u1']//a[@name='tj_settingicon']")

# 2、鼠标移到某一个元素上，弹出下拉列表
ActionChains(driver).move_to_element(ele).perform()

# 3、选择下拉列表中的“高级搜索”点击
# 方式一:根据文本内容定位 contains(text())
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//a[text()="高级搜索"]')))
driver.find_element_by_xpath('//a[text()="高级搜索"]').click()

# 4、找到select元素
# 点击之后的等待
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//select[@name='ft']")))
select_ele = driver.find_element_by_xpath("//select[@name='ft']")

# 5、实例化select类
s = Select(select_ele)

# 6、选择下拉列表值
# 方式一：下标从0开始
s.select_by_index(4)
time.sleep(1)

# 方式二:value值选
s.select_by_value("pdf")
time.sleep(1)

# 方式三：文本内容
s.select_by_visible_text("所有格式")

