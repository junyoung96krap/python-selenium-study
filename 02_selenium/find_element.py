# find_element() 메소드에게 내가 원하는 요소의 정보를 매개변수로 넘겨주면 해당 요소가 지정됨.
# click() 메소드로 마우스 왼쪽 클릭을 수행.

import time
from selenium import webdriver
from selenium.webdriver.common.by import By # by 지정자 사용 시 작성.

driver = webdriver.Chrome()
driver.get('http://naver.com')
driver.implicitly_wait(10) # 코드를 대기시키는 코드 (time.sleep과 다름)

driver.find_element(By.ID, 'account').click()
time.sleep(5)

# By 지정자로 찾을 수 있는 속성들

# CSS_SELECTOR
# CLASS_NAME
# ID
# XPATH
# LINK_TEXT
# NAME
# PARTIAL_LINK_TEXT
# TAG_NAME
# 여러 종류의 속성을 지원하지만 주로 위에서 4개의 속성으로 엘리먼트를 찾음.

driver.get('https://www.cgv.co.kr')
driver.implicitly_wait(10)

driver.find_element(By.CLASS_NAME, 'mmns00008_today__ad1TX').click()
driver.find_element(By.XPATH, '//*[@id="contentArea"]/div[2]/div/div/div[1]/div[2]/button').click()
driver.find_element(By.CSS_SELECTOR, '#contentArea > div > div:nth-child(2) > div > section > div > ul > li:nth-child(1) > div.bestChartList_btnArea__0T7cm > button.btn.btn-md.line-gray').click()
time.sleep(5)
