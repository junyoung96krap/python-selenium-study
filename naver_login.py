# TC - 네이버 로그인

# TC ID: NAVER_LOGIN_001
# 테스트 목적: 네이버 로그인 기능이 정상적으로 동작하는지 확인한다.

# 사전 조건
# 네이버 홈페이지에 접속한다.
# 로그인에 사용할 테스트 계정이 준비되어 있다.

# 테스트 절차
# 네이버 홈페이지에 접속한다.
# 로그인 버튼을 클릭한다.
# 아이디 입력창에 테스트 아이디를 입력한다.
# 비밀번호 입력창에 테스트 비밀번호를 입력한다.
# 로그인 버튼을 클릭한다.
# 로그인 결과를 확인한다.

# 기대 결과
# 로그인 버튼 클릭 시 로그인 페이지로 정상 이동한다.
# 아이디와 비밀번호가 정상적으로 입력된다.
# 로그인 버튼 클릭 후 정상적으로 로그인된다.
# 로그인 성공 후 로그인된 상태를 확인할 수 있는 요소가 화면에 표시된다.

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.naver.com/')
driver.implicitly_wait(10)

driver.find_element(By.CLASS_NAME, 'MyView-module__link_login___VlF7z').click()
driver.implicitly_wait(10)

elem_id = driver.find_element(By.CSS_SELECTOR, '#id')
elem_id.click()
elem_id.send_keys('test')

elem_pw = driver.find_element(By.CSS_SELECTOR, '#pw')
elem_pw.click()
elem_pw.send_keys('test')

driver.find_element(By.CSS_SELECTOR, '#loginBtn_row').click()

if driver.find_element(By.CSS_SELECTOR, '#frmNIDLogin > div:nth-child(21) > div > h2').is_displayed():
    print('보안을 위해 추가 확인 필요')
    result = 'PASS'
else:
    print('보안을 위해 추가 확인 필요 없음')
    result = 'FAIL'

print('테스트 결과: ', result)
time.sleep(20)