"""

@date: 2020/3/25 22:40 
@author：Spring
"""

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://ke.qq.com/')
driver.find_element_by_xpath("//*[@id='js_login']").click()
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(
        (By.XPATH, "//*[@class='ptlogin-wrap']//a[@class='js-btns-enter btns-enter btns-enter-qq']")))
driver.find_element_by_xpath("//*[@class='ptlogin-wrap']//a[@class='js-btns-enter btns-enter btns-enter-qq']").click()

# 代表进入了另一个界面
# 等待iframe存在，可见

# 方式一  显示等待 进入
path = '//div[@class="mod-tab__content-wrap mod-tab__content-wrap_qq"]//iframe'
# # 定位表达式
driver.switch_to.frame(driver.find_element_by_xpath(path))
time.sleep(0.5)

# 方式二  frame_to_be_available_and_switch_to_it
# WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it('path'))
# time.sleep(0.5)

driver.find_element_by_id('switcher_plogin').click()

# 从iframe中回到默认的页面当中
driver.switch_to.default_content()
