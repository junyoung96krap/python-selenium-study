# pyautogui 모듈
# Python 코드로 브라우저에 한정되지 않고 마우스와 키보드를 자동으로 제어할 수 있는 기능을 제공.
# 그 외에도 스크린샷을 촬영하거나 이미지 인식 등의 기능도 제공함.

# Selenium 보다 간단한 방법으로 제어가 가능하지만 Selenium의 기능이 더 강력함.

import pyautogui
import time
from selenium import webdriver

driver = webdriver.Chrome()

mouse_position = pyautogui.position()
print(mouse_position) # 현재 마우스의 위치
print(mouse_position[0]) # x좌표
print(mouse_position[1]) # y좌표
# 튜플 형태로 반환해 주기 때문에 인덱스로 각 요소에 접근이 가능하다.
# 튜플 : 리스트와 비슷하지만 요소를 수정 할 수는 없음.

# 마우스 제어
pyautogui.moveTo(0, 0) 

driver.maximize_window()
driver.get('https://naver.com/')
driver.implicitly_wait(10)
pyautogui.click(1300, 300)

pyautogui.click(button='right')
pyautogui.doubleClick()
time.sleep(10)

# 키보드 제어
pyautogui.typewrite('toy story', interval=0.1)
pyautogui.press('enter')

pyautogui.keyDown('ctrl')
pyautogui.press('a')
pyautogui.keyUp('ctrl')
time.sleep(5)