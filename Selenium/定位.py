"""
等待时间
    显示等待
    隐性等待
        driver.implicitly_wait()
    强制等待
@date: 2020/3/25 15:02 
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

# # 隐性等待
# driver.implicitly_wait(4)


# 显性等待
xpath = "//p[@class='tang-pass-footerBarULogin pass-link']"
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))

driver.find_element_by_xpath(
    "//*[@class='tang-pass-footerBar']//p[@class='tang-pass-footerBarULogin pass-link']").click()

# 条件 EC.visibility_of_element_located((By.XPATH, xpath))


# 代表进入了另一个界面
# 等待iframe存在，可见

# 方式一
id = '//div[@class="mod-tab__content-wrap mod-tab__content-wrap_qq"]//iframe'
driver.switch_to.frame(id)
# 定位表达式
driver.switch_to.frame(driver.find_element_by_xpath('//div[@class="mod-tab__content-wrap '
                                                    'mod-tab__content-wrap_qq"]//iframe'))
time.sleep(0.5)

# 方式二  iframe切换
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it('id'))
time.sleep(0.5)

driver.find_element_by_id('switcher_plogin')


# 从iframe中回到默认的页面当中
driver.switch_to.default_content()


# 切换二
# 窗口切换
# step1:获取窗口的总数及句柄
# handles是一个列表 ，新打开的窗口位于最后
handles=driver.window_handles


driver.switch_to.window()