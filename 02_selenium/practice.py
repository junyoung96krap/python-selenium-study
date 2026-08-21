# 1. Selenium과 Python을 이용해 임의의 페이지 5개에 접근하기.
# 2. 접근한 페이지들의 타이틀을 title = [] 리스트에 추가하기.
# 3. 접근한 페이지들의 url을 url = [] 리스트에 추가하기.
# 4. title 리스트와 url 리스트를 출력하는 코드를 작성하기.

import time
from selenium import webdriver

driver = webdriver.Chrome()

titles = []
urls = []

pages = ['http://naver.com', 'http://google.com', 'https://youtube.com', 'https://github.com', 'https://comento.kr']

for page in pages:
    driver.get(page)
    titles.append(driver.title)
    urls.append(driver.current_url)

print(titles)
print(urls)

driver.quit()

# 타이틀만 출력해보기 (챗지피티 연습문제)

# titles = []

# pages = ['https://www.naver.com', 'https://www.google.com', 'https://www.youtube.com']

# for page in pages:
#     driver.get(page)
#     titles.append(driver.title)

# print(titles)
