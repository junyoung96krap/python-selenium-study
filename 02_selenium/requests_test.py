# requests 모듈

# 파이썬 코드에서 웹 페이지에 요청을 보내고 응답을 받아오는 모듈
# HTML 소스코드, HTTP 상태 코드를 받을 수 있다

# 대표적으로 GET 방식의 요청과 POSD 방식의 요청을 보낼 수 있음.
# GET 방식 : 서버에서 데이터를 읽어올 떄 사용!
# POST 방식 : 서버에 데이터를 생성하거나 업데이트 할 때 사용! (api 테스트 진행 할 때 사용 가능)

# requests 모듈로 서버에서 데이터를 읽을 수도, 생성할 수도, 업데이트 할 수도 있다!


# GET 요청 > 서버의 데이터를 조작하지 않고 현재 상태 그대로 가져온다.

import requests

response = requests.get('https://naver.com')
print(response.text)
# 네이버의 HTML 데이터를 읽어온다.

print(response.status_code)
# 네이버의 HTTP 상태 코드를 읽어온다.

# Selenium + Requests

# Selenium 모듈의 get_log('browser') 메소드로 프론트 단의 상태를 확인.
# Requests 모듈의 response.status_code로 네트워크, 서버 상태를 확인.

# 프론트 + 네트워크 + 서버의 상태를 확인할 수 있음.

