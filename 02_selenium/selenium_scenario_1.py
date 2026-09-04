# 연습하기
# 1. 유저 시나리오를 TC화 하기
#   a. cgv 홈페이지에 접속해 영화 이름을 검색한다.
#   b. 존재하지 않는 영화 이름을 검색한다.
#   c. 존재하지 않는 영화 검색 시 결과 페이지를 확인한다.
#   d. 한글 영화 이름을 검색한다.
#   e. 영문 영화 이름을 검색한다.
#   f. 특수문자가 포함된 영화 이름을 검색한다.
#   g. 영화 상세 정보로 이동한다.
#   h. cgv 로고를 클릭하여 홈으로 이동한다.
# 2. TC를 자동화 하기
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://cgv.co.kr/')
driver.implicitly_wait(10)

# 오늘은 그만보기 선택
driver.find_element(By.CLASS_NAME, 'mmns00008_today__ad1TX').click()

#   a. cgv 홈페이지에 접속해 영화 이름을 검색한다.
driver.find_element(By.CSS_SELECTOR, 'body > div:nth-child(1) > div > div > div > div > div.mets01390_mainContentArea__GkUrT > div > header > div > div > div > button:nth-child(3) > svg').click()
elem = driver.find_element(By.CLASS_NAME, 'txt-input')
#   b. 존재하지 않는 영화 이름을 검색한다.
elem.send_keys('asdasd')
#   c. 존재하지 않는 영화 검색 시 결과 페이지를 확인한다.
driver.find_element(By.CSS_SELECTOR, '#contentArea > div > div.top-fix-wrapper > div > div > div > div > button > svg').click()
driver.implicitly_wait(10)

elem_text = '영화 또는 인물명을 확인 후 다시 검색해 주세요.'
if elem_text == driver.find_element(By.CSS_SELECTOR, '#contentArea > div > div.tmes01040_section__D67K1.pdt-40 > div > p').text:
    print('존재하지 않는 영화 검색 성공!')
else:
    print(elem_text)
    print('존재하지 않는 영화 검색 실패!')

#   d. 한글 영화 이름을 검색한다.
elem.clear()
elem.send_keys('오디세이')
driver.find_element(By.CSS_SELECTOR, '#contentArea > div > div.top-fix-wrapper > div > div > div > div > button > svg').click()
driver.implicitly_wait(10)

elem_text = '상세보기'
if elem_text == driver.find_element(By.CLASS_NAME, 'btn.btn-md.line-gray').text:
    print('한글 영화 이름 검색 성공!')
else:
    print('한글 영화 이름 검색 실패!')

#   e. 영문 영화 이름을 검색한다.
elem.clear()
elem.send_keys('WANNA ONE GO in LA')
driver.find_element(By.CSS_SELECTOR, '#contentArea > div > div.top-fix-wrapper > div > div > div > div > button > svg').click()
driver.implicitly_wait(10)

elem_text = '상세보기'
if elem_text == driver.find_element(By.CLASS_NAME, 'btn.btn-md.line-gray').text:
    print('영문 영화 이름 검색 성공!')
else:
    print('영문 영화 이름 검색 실패!')

#   f. 특수문자가 포함된 영화 이름을 검색한다.
elem.clear()
elem.send_keys('스파이더맨-브랜드 뉴 데이')
driver.find_element(By.CSS_SELECTOR, '#contentArea > div > div.top-fix-wrapper > div > div > div > div > button > svg').click()
driver.implicitly_wait(10)

elem_text = '상세보기'
if elem_text == driver.find_element(By.CLASS_NAME, 'btn.btn-md.line-gray').text:
    print('특수문자가 포함된 영화 이름 검색 성공!')
else:
    print('특수문자가 포함된 영화 검색 실패!')
#   g. 영화 상세 정보로 이동한다.
driver.find_element(By.CLASS_NAME, 'btn.btn-md.line-gray').click()
driver.implicitly_wait(10)

if driver.find_element(By.CLASS_NAME, 'cnms01020_prologSection__ICKvf').is_displayed():
    print('상세 정보 페이지 이동 성공!')
else:
    print('상세 정보 페이지 이동 실패!')

#   h. cgv 로고를 클릭하여 홈으로 이동한다.
driver.find_element(By.CSS_SELECTOR, 'body > div:nth-child(1) > div > div > div > div > div.mets01390_mainContentArea__GkUrT > div > header > div > div > div.icon-btn-wrap.left-wrap > button:nth-child(2) > svg').click()
driver.implicitly_wait(10)

if driver.find_element(By.CLASS_NAME, 'logo-link').is_displayed():
    print('홈으로 이동 성공!')
else:
    print('홈으로 이동 실패!')

time.sleep(10)

