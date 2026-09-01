# Selenium 코드 제어하기
# 대기
# 묵시적 대기 : implicitly_wait()
# 페이지 로딩에 완료될때 까지 최대 n초간 기다리고, 그 이후에도 로딩이 되지 않으면 에러를 발생시켜라!

# 명시적 대기 : explictily_wait
# 내가 지정한 ~객체가 페이제 표시될 때 까지 기다려라! (서버단에서 로직이 돌고있거나, 렌더링 중이어서 화면에 아직 표시가 안되었을수도 있으니)
# 코드가 길어짐.

# 무조건 대기 : time.sleep()
# 한 페이지 내에서 동작을 수행할 때
# 애니메이션이 있는 엘리먼트의 애니메이션이 완료되길 기다릴 때
# 페이지에서 반드시 n초 이상의 대기시간이 필요할 때. 
# 등등..

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://www.baemin.com')
driver.implicitly_wait(10)