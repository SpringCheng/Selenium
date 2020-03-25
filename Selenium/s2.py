"""

@date: 2020/3/24 18:21 
@author：Spring
"""

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
# method 1
ele = driver.find_element_by_id('kw')
print(ele.get_attribute('class'))

# method 2
eles = driver.find_elements_by_class_name('s_ipt')
ele1 = driver.find_element_by_class_name('s_ipt_wr')


