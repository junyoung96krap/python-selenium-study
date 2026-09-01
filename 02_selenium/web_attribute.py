# 브라우저 조작하기
# 1. 원하는 특정 페이지에 접속하기.
# 2. 임의의 엘리먼트를 선택해 get_attribute() 메소드로 속성 값을 출력하기. (있는 경우와 없는 경우 분기 처리)
# 3. 임의의 엘리먼트의 text 추출하기.(있는 경우와 없는 경우 분기처리)
# 4. 임의의 엘리먼트의 location 정보를 추출하기 각 key를 호출해 value를 하나씩 출력하기.

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.coupang.com')
driver.implicitly_wait(10)

elem = driver.find_element(By.ID, 'wa-category')

if elem.get_attribute('href') is None:
    print('href 가 존재하지않습니다.')
else:
    print(elem.get_attribute('href'))

if elem.text == '':
    print('text 가 존재하지않습니다.')
else:
    print(elem.text)

print(elem.location['x'])
print(elem.location['y'])