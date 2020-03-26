"""
Keys.CONTRL=Ctrl
keys.CONTROL=Ctrl
send_keys(keys.CONTROL,'a')
	Ctrl+a
send_keys(keys.CONTROL,'x'') Ctrl+x
send_keys(keys.CONTROL,'c')
	Ctrl+'c'
Keys.Enter
Keys.BACK_SPACE
keys.SPACE
keys.TAB

@date: 2020/3/26 16:47 
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
driver.find_element_by_id('kw').send_keys("python", Keys.ENTER, Keys.CONTROL, 'a')
