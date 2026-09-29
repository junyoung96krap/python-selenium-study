# 테스트 결과 리포트 폴더 만들기

# 현재 경로에 test_result 폴더가 없으면 만들어라.
import os

if not os.path.exists('test_result'):
    os.makedirs('test_result')

# f = open('파일 경로/파일명', '모드')
# r 모드 = 파일 읽기 (파일이 없는 경우 오류 발생)
# w 모드 = 파일 쓰기 (파일이 없는 경우 파일을 만듦, 파일이 있으면 내용을 덮어씀)
# x 모드 = 파일 쓰기 (파일이 없는 경우 파일을 만듦)
# a 모드 = 파일 추가 (파일이 있으면 맨 끝에 내용을 추가함)

f = open('test_result/test_result.txt','w')
f.write('내용을 작성합니다.')

f = open('test_result/test_result.txt','a')
f.write('\n내용을 추가합니다.')
f.close()

# f.close() >> 열었던 파일(f)를 닫는 closed() 메소드. 
# 파일을 닫지 않으면 다른 코드에서 이미 열려있는 파일을 또 열려고 시도할 떄 충돌이 발생함.
