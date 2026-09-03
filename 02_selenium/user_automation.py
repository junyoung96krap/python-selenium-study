# 유저 액션 자동화

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://cgv.co.kr/')
driver.implicitly_wait(10)

driver.find_element(By.CLASS_NAME, 'mmns00008_today__ad1TX').click()
driver.find_element(By.CSS_SELECTOR, 'body > div:nth-child(1) > div > div > div > div > div.mets01390_mainContentArea__GkUrT > div > header > div > div > div > button:nth-child(3)').click()

elem = driver.find_element(By.ID, 'swrd')
elem.click()
elem.send_keys('토이스토리') # 입력값 명령어 send_keys
elem.clear()
elem.send_keys('오디세이')

driver.find_element(By.CSS_SELECTOR, '#contentArea > div > div.top-fix-wrapper > div > div > div > div > button').click()

# 페이지 스크롤
driver.execute_script("window.scrollTo(0, 100)")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

# ActionChain

# click()
# double_click()
# click_and_hold()
# move_to_element()
# key_down()
# key_up()
# send_keys()
# send_keys_to_element()

time.sleep(10)

# 대상을 찾고 > 상태를 체크하고 > 흐름을 제어하며 > 액션을 전달한다
# 이 과정을 모으고, 반복하면 자동화 스크립트 완성