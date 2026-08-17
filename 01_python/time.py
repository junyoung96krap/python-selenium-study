# 내장 모듈
# time : 시간과 관련된 기능들..

# time 모듈의 strftime 함수에서 제공하는 기능을 이용해 현재 시간을 출력하는 예제.
import time

nowStamp = time.time()
now = time.strftime('%H:%M', time.localtime(nowStamp))
print(now)

# time 모듈의 sleep 함수를 사용하면 코드 진행을 일시 정지 시킬 수 있다.
print('시작')
time.sleep(3)
print('끝')