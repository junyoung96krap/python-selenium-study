# 테스트 결과 리포트
# 결과 리포트에 포함하고 싶은 내용.

# 테스트 수행 날짜
# TC ID
# TC 실행 결과
# 성공 TC 개수
# 실패 TC 개수
# TC 실패 이유
# TC 실행 개수/전체 개수
# 진척률
# 성공률

# 현재 시간 구하기
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

now = time.strftime('%y_%m_%d_%H_%M')
result_pass_list = [] # pass 한 tc id를 가지고 있는 리스트
result_fail_list = [] # fail 한 tc id를 가지고 있는 리스트
fail_reason_list = [] # fail 한 원인을 가지고 있는 리스트
tc_count = 2 # 전체 tc 카운트

# 테스트 전 과정에 걸쳐 에러발생 시 에러 기록하는 try, except 문
try:
    f = open(f'test_result/{now}_test_result.txt', 'w')
    f.write(f'테스트 수행 일자 - {now}\n')

    # TC_001 CGV 홈페이지 접속
    tc_progress = 'TC_001'
    driver = webdriver.Chrome()
    driver.maximize_window()

    start_time = time.time()
    driver.get('https://cgv.co.kr/')
    driver.implicitly_wait(10)
    end_time = time.time()

    driver.find_element(By.CLASS_NAME, 'mmns00008_today__ad1TX').click()

    try:
        if driver.find_element(By.CLASS_NAME, 'mets01390_logo__sm8Za').is_displayed():
            print('TC_001 로고 노출, 페이지 로딩 PASS')
            result_pass_list.append(tc_progress)

    except Exception as e:
        fail_reason = 'CGV 로고 미노출, 페이지 로딩 FAIL'
        print('fail_reason')
        result_fail_list.append(tc_progress)
        fail_reason_list.append(fail_reason)

    # TC_002 FAIL 만들기
    tc_progress = 'TC_002'

    start_time = time.time()

    driver.get('https://cgv.co.kr/')

    end_time = time.time()

    loading_time = end_time - start_time

    print(f'{tc_progress} 페이지 로딩 시간 : {loading_time:.2f}초')

    if loading_time <= 0:
        print(f'{tc_progress} PASS')
        result_pass_list.append(tc_progress)

    else:
        fail_reason = f'페이지 로딩 시간이 0초를 초과함 ({loading_time:.2f}초)'
        print(f'{tc_progress} FAIL')
        result_fail_list.append(tc_progress)
        fail_reason_list.append(fail_reason)

except Exception as e :
    print(f'에러 발생하여 테스트 스크립트 종료. {tc_progress} >>> {e}')

# 테스트 결과를 수집한 리스트

# PASS 테스트 결과 기록
f.write('\n[RESULT - PASS]\n')
for pass_cnt in range(len(result_pass_list)):
    f.write(f'{result_pass_list[pass_cnt]} : PASS\n')

# FAIL 테스트 결과 기록
f.write('\n[RESULT - FAIL]\n')
for fail_cnt in range(len(result_fail_list)):
    f.write(f'{result_fail_list[fail_cnt]} : FAIL\n')
    f.write(f'\tFAIL REASON : {fail_reason_list[fail_cnt]}\n')

f.write('\n')
f.write(f'PASS TC COUNT : {len(result_pass_list)}\n') # PASS TC 개수
f.write(f'FAIL TC COUNT : {len(result_fail_list)}\n')# FAIL TC 개수
f.write(f'COMPLETED TEST COUNT : {len(result_pass_list) + len(result_fail_list)}\n')# 수행 완료한 TC 개수
f.write(f'PROGRESS OF TEST : {((len(result_pass_list) + len(result_fail_list))/tc_count) * 100}%\n')# TC 진척률
f.write(f'PASS RATE : {(len(result_pass_list)/tc_count)*100}%\n')# PASS TC 비율
