# 예외처리
# try, except
# 어떤 이유로든 코드 실행 시 에러가 발생하면 코드 실행이 종료됨.
# 흔히 "~가 죽었다.", "강제종료 되었다." 라고 표현할 때의 그 상황.
# 예외처리 구문은 에러가 발생했을 때 코드 실행이 종료되지 않고, 대비해 둔 코드로 이동하여 해당 코드를 실행하도록 함.

# 에러 발생 지점 전까지 코드가 실행되고, 에러가 발생하는 순간 except 문의 코드를 실행한다.
# 그 이후의 코드도 계속해서 실행됨!
try:
    if 5/0 >= 1:
        print('1보다 크다.')
    else:
        print('1보다 작다.')
    print('계산 종료')
except Exception as e:
    print(f'나눗셈 에러 발생!! >> {e}')

# Exception 에러를 명시하지 않고 모든 에러를 예외처리.

print('에러 발생 이후 코드!')

# 예외가 발생할 수 있는 상황
# 1. 0으로 나누기.
# 2. 리스트 크기보다 더 큰 인덱스로 요소에 접근하기.
# 3. 숫자와 문자열을 합치기.
# 4. selenium에서는 어떤 에러가 발생하는가? > 웹드라이버 설정 오류, 요소 인식 안됨 등등

# 1

try:
    if 5/0 >= 1:
        print('1보다 크다.')
    else:
        print('1보다 작다.')
except Exception as e:
    print(f'에러 발생 {e}')

# 2

try:
    a = [0, 1, 2]
    print(a[3])
except Exception as e:
    print(f'에러 발생 {e}')

# 3 

try:
    b = 4
    c = '합치기'
    print(b + c)
except Exception as e:
    print(f'에러발생 {e}')