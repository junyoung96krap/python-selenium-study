# 예외처리

# 페이지 접속 실패
# - 코드 실행 시 웹 브라우저 자체에서 오류가 발생한 경우
# - WebDriverException 발생.
# - 네트워크 상태 확인, 재접속 시도, URL 오타 확인, WebDriver 경로 확인 등..
# - 코드 진행을 멈추고 원인 파악이 필요한 환경 설정에 대한 문제일 확률이 큼.

# 엘리먼트 로딩 실패
# 엘리먼트 인식 실패
# - NoSuchElementException 에러 발생
# - 필요한 조치 : 재접속 시도, refresh(), URL 오타 확인, 엘리먼트 지정자 오타 확인 등..
# - try ~ except 문으로 예외처리, 코드 수정 필요.

# 웹 페이지 에러내용 확인하기 
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://comento.kr/?index')
error_log = driver.get_log('browser')
print(error_log)
print(error_log[0])
print(error_log[0]['level'])

# 자주 만날 수 있는 에러 레벨
# INFO : 정보
# WARNING : 경고
# SEVERE : 심각한 오류
