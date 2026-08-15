# 반복문
# 하나의 작업을 여러 번 반복 수행하는 구문.
# while, for
# while(조건식): > 조건식이 True이면 명령을 계속 반복한다. False 가 되면 정지
cnt = 0

while(cnt < 10):
    print(f'{cnt + 1} 번째 반복')
    cnt += 1

# flag 를 이용하여 반복을 제어하는 방법
flag = 0
cnt = 0

while(flag == 0):
    if cnt == 5:
        flag = 1
    else:
        print(f'{cnt + 1}번째 반복')
        cnt += 1

# for 문 
# for 변수 in range (시작하는 값, 끝나는 값, 연속 갑의 차):
for a in range (0, 5, 1):
    print(a)

for a in range(0, 5, 2):
    print(a)

for a in range(5, 0, -1):
    print(a)

# 세번째 인자인 연속값의 차는 디폴트 1이며 생략이 가능하다.
for a in range(0, 5):
    print(a)

# 리스트를 출력하기
# 리스트를 반복문 없이 통째로 출력하거나, 인덱스를 이용해 개별 출력할 수 있다.
a = [1, 2, 3, 4, 5]
print(a)

print(a[0])
print(a[1])

# 반복문을 이용하면 중복된 코드없이 리스트의 데이터를 원하는 만큼 출력할 수 있다.
a = [1, 2, 3, 4, 5]
for index in range(0, 5):
    print(a[index])

# break문은 자신이 속해있는 반복문을 종료하고 다음 코드로 넘어간다.
for a in range(0, 5):
    if a == 3:
        print('a가 3이 되어 반복을 종료합니다.')
        break
    else:
        print(a)

# contine를 만나면 같은 블록의 다음코드를 실행하지 않고 다음으로 넘어간다.
for a in range(10):
    if a % 2 == 1:
        continue
    print(a)

# 연습하기
# for 문을 이용하여 1 ~ 10까지의 합을 구하기.
total = 0

for a in range(1, 11):
    total += a

print(total)


# for 문을 이용하여 a = [1, 2, 3, 4, 5]를 역순으로 출력하기
a = [1, 2, 3, 4, 5]

for i in reversed(a):
    print(i)

a = [1, 2, 3, 4, 5]

for i in range(4, -1, -1):
    print(a[i])