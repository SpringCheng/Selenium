"""

@date: 2020/3/26 17:40 
@author：Spring
"""

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.find_element_by_id('kw').send_keys('柠檬班', Keys.ENTER)

WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'首页- ')]")))

ele = driver.find_element_by_xpath("//a[contains(text(),'首页- ')]")

# 使用js进行滚屏操作
driver.execute_script("arguments[0].scrollIntoView(false);", ele)
# driver.execute_script("window.scrollTO(doucument.body.scrollHeight,0")
# driver.execute_script("window.scrollTo(doucment.body.scrollHeight,0")
# driver.execute_script("window.scrollTo(0,body.scrollHeight")
