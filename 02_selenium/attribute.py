# 웹 엘리먼트 속성 다루기
# <attribute> 웹 엘리먼트의 다양한 속성 값을 추출하고 데이터로써 사용하는 방법.
# 속성값(get_attribute())
# 문자 데이터(Text)
# 화면 상의 위치(location)
# 엘리먼트의 크기(size) 등등..

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://cgv.co.kr/')
driver.implicitly_wait(10)

driver.find_element(By.CLASS_NAME, 'mmns00008_today__ad1TX').click()

elem = driver.find_element(By.CSS_SELECTOR, '#contentArea > div.main-padding.main-first-conponent > div > div > div.mainMovieChart_slideFilterArea__DsVP3 > div.mainMovieChart_btnWrap__zmlGa > button')

print(elem.get_attribute('class'))
print(elem.text)
print(elem.location)
print(elem.size)

size_info = elem.size

if size_info['height'] < size_info['width']:
    print('가로가 길다.')
elif size_info['height'] > size_info['width']:
    print('세로가 길다')