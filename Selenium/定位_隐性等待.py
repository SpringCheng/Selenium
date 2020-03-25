"""

@date: 2020/3/25 21:42 
@author：Spring
"""


from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.find_element_by_xpath("//*[@id='u1']//a[@name='tj_login']").click()

# 隐性等待
driver.implicitly_wait(4)