# f-string formatting (python 3.6 버전부터 지원)
# 문자열을 생성하는 방식 중 하나.
# f'' 로 시작하여 중괄호{} 안에 변수 또는 표현식을 넣어 사용 할 수 있다.

a=5
print(a)

a=8
print(a)

a=5
b=3

print(f'a + b = {a+b}')

a=8
b=3

print(f'a + b = {a+b}')

age=10
name='csdo'

print(f'My name is {name}, I\'m {age} years old.')

# 연습하기
# 변수이 10, 20, 30을 할당해 아래 문자열을 출력하세요.

a=10
b=20
c=30
print(f'{a} 더하기 {b} 은 {c} 입니다.')

# 저는 대한민국의 서울에 살고 있습니다.
a='대한민국'
b='서울'

print(f'저는 {a}의 {b}에 살고 있습니다.')

# 범죄신고는 112.
a=112

print(f'범죄신고는 {a}.')

# 변경사항 github 확인