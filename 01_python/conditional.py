# 조건문
# 조건식에 따라 실행되는 코드를 제어 (True, False)
# 코드 블록을 구분하기 위한 문법으로 4칸 또는 tab 키를 사용.
# 지키지 않으면 IndentationError 오류 발생!

a = 20
if a > 10:
    print('a는 10보다 큽니다.')

if a < 10:
    print('a는 10보다 작습니다.')

# 홀수, 짝수 구하기
a = 20
if a % 2 == 0:
    print('a는 짝수입니다.')

if a % 2 == 1:
    print('a는 홀수입니다.')

# 입력받기 input() > input은 기본적으로 str으로 받아옴.
a = input('정수를 입력해 주세요.')
if int(a) % 2 == 0:
    print('a는 짝수입니다.')

if int(a) % 2 == 1:
    print('a는 홀수입니다.')

# elif == else if
a = int(input('정수를 입력해주세여 : '))

if a % 2 == 0:
    print('a는 짝수입니다.')
elif a % 2 == 1:
    print('a는 홀수입니다.')

# if vs elif
# 동작성은 같음. 같은 데이터의 조건을 비교하기 위한 if가 많을수록 비효율적이다.

# else > 위의 조건들이 모두 false 일 때 실행
a = int(input('정수를 입력해 주세요.'))

if a % 2 == 0:
    print('a는 짝수입니다.')
elif a % 2 == 1:
    print('a는 홀수입니다.')
else:
    print('다시 입력해 주세요.')

# 연습하기
# 나이를 입력받고, 20세 이상이면 성인, 20세 미만이면 미성년자 라고 출력하기.
age = int(input('나이를 입력하세요 : '))

if age >= 20:
    print('성인')
else:
    print('미성년자')

# 점수를 입력받고 90점 이상이면 A, 80점 이상이면 B, 70점 이상이면 C, 60점 이상이면 D, 60점 미만이면 F 학점이라고 출력하기.
score = int(input('점수를 입력하세요 :'))

if score >= 90:
    print('A 학점')
elif score >= 80:
    print('B 학점')
elif score >= 70:
    print('C 학점')
elif score >= 60:
    print('D 학점')
elif score < 60:
    print('F 학점')

# 길이가 10인 리스트에 1~10까지 할당하고, 인덱스를 입력받으면 해당 요소가 홀수인지, 짝수인지 출력하기.
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
index = int(input('인덱스를 입력해주세요 : '))

if a[index] % 2 == 0:
    print('짝수')
elif a[index] % 2 == 1:
    print('홀수')