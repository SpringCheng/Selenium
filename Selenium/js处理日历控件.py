"""
12306官网
1、使不能输入的readOnly改为false
    ele=document.getElementById('train_date')
    ele.readOnly= false
3、移除该属性
    ele=document.getElementById('train_date')
    ele.removeAttribute('readonly')

@date: 2020/3/26 18:27 
@author：Spring
"""

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.12306.cn')

js = "var ele=document.getElementById('train_data');ele.readonly=false;ele.value='2020-3-28';"
jd = "var lel=doucment.getElementById('search_one');lel.click();"
# execute_script()执行js代码
driver.execute_script(js)
driver.execute_script(jd)

