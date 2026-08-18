# Selenium
# 가장 많이 사용되는 브라우저 자동화 라이브러리 중에 하나.
# 크롬, 엣지, 파이어폭스, 사파리, 오페라 등 주요 브라우저 지원.
# 다양한 프로그래밍 언어에서 거의 동일한 API를 이용해 자동화 구현이 가능하도록 지원함.
# 마우스, 키보드 제어, 웹 페이지 엘리먼트 검사, 검색 등의 기능 제공.

# 외장 라이브러리 : selenium
# 설치 : pip install selenium
# Selenium version 확인 : pip show selenium

from selenium import webdriver
driver = webdriver.Chrome()

# 웹 드라이버
# 셀레니움으로 브라우저를 자동화 할 때 사용하는 드라이버.
# 셀레니움을 통해 브라우저를 제어할 수 있게 해줌.

# 웹 드라이버 관리
# 1. 수동 관리
# 2. 자동 관리 (Selenium v4.0.0 이상 지원)