"""
alert切换
弹窗
@date: 2020/3/25 17:28 
@author：Spring
"""

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
# driver.get('https://www.baidu.com')
# driver.find_element_by_id('kw').send_keys("柠檬班")
# driver.find_element_by_id('su').click()
#
# WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'吧_百度贴吧')]")))


#
driver.get('D:\\Practice\\Pycharm\\Lemon\\HTML\\web UI.html')
WebDriverWait(driver, 2).until(EC.alert_is_present())

# alert切换
alert = driver.switch_to.alert
# 切换
# 接受
# alert.accept()
# 拒绝
# alert.dismiss()
print(alert.text)
alert.dismiss()
