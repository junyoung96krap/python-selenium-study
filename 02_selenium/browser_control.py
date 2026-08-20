# 브라우저 조작하기

import time
from selenium import webdriver

driver = webdriver.Chrome()

# 브라우저 최대
driver.maximize_window()
time.sleep(5)

# 브라우저 최소
driver.minimize_window()
time.sleep(5)

# 브라우저 위치를 지정
driver.set_window_position(500, 0)
time.sleep(5)

# 브라우저의 크기를 지정
driver.set_window_size(500, 500)
time.sleep(5)

# 브라우저의 위치와 크기를 지정하는 이유
# 1. 사용자 환경마다 모니터의 해상도, 크기가 다름.
# 2. 사용자 환경마다 모니터의 개수가 다름.
# 3. 이런 이유로 사용자 환경마다 브라우저의 위치가 달라짐.
# 4. 좌표를 기준으로 작성한 자동화 테스트는 실행 불가.
# 브라우저의 위치와 크기를 지정하면 위의 문제들이 해결됨!

# 웹 페이지의 접근하기
driver.get('http://naver.com') 
time.sleep(5)

# 웹 페이지의 타이틀 출력
driver.get('http://naver.com')
print(driver.title)
time.sleep(5)

# 현재 웹 페이지의 URL 출력 (주로 실패한 케이스에서 실패 지점으로 바로 이동할 수 있는 링크를 제공하여 현상 확인을 위해 사용함.)
driver.get('http://naver.com')
print(driver.current_url)
time.sleep(5)

# 브라우저 새로고침
driver.get('http://naver.com')
driver.refresh()
time.sleep(5)

# 브라우저 뒤로가기
driver.get('http://naver.com')
driver.back()
time.sleep(5)

# 브라우저 앞으로 가기
driver.get('http://naver.com')
driver.forward()
time.sleep(5)

# 테스트 종료하기 (실행중인 브라우저와 웹드라이버를 종료함. 웹 드라이버가 완전히 종료되지 않아 메모리 누수가 발생할 수 있음.)
driver.quit()
time.sleep(5)

# 연습하기
# 1. 브라우저의 크기를 최대화 하기.
# 2. 원하는 특정 페이지에 접속하기.
# 3. 해당 페이지의 타이틀과 url을 출력하기.
# 4. 브라우저의 위치와 크기를 조정하기.
# 5. 또다른 페이지에 접속하기.
# 6. 새로 접속한 페이지의 타이틀과 정보를 출력하기.

driver.maximize_window()

driver.get('http://google.com')
print(driver.title)
print(driver.current_url)

driver.set_window_position(0, 0)
driver.set_window_size(600, 600)

driver.get('http://naver.com')
print(driver.title)
print(driver.current_url)

time.sleep(5)