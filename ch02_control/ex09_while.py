# 파이썬 기초 (+카카오톡 챗봇) 스터디 1주차

# python 제어문
# 2. 반복문 while

# 2.1 기본 형태
print("\n[ 2.1 기본 형태 ] ─────────────────────────────────────────────────────────────────────────────────────────\n")

i = 0
while i < 10:
    i = i + 1
    print("나무를 %d번 찍었습니다." % i)
    if i == 10:
        print("나무 넘어갑니다.")

# 2.2 break
print("\n[ 2.2 break ] ─────────────────────────────────────────────────────────────────────────────────────────────\n")

answer = 55
minValue = 1
maxValue = 100
msg = "%d 부터 %d 사이의 숫자를 입력해주세요: " % (minValue, maxValue)

while True:
    comparison = int(input(msg))
    if comparison >= maxValue:
        msg = "입력하신 값은 %d 보다 큽니다. %d 부터 %d 사이의 숫자를 입력해주세요: " % (maxValue, minValue, maxValue)
    elif comparison <= minValue:
        msg = "입력하신 값은 %d 보다 작습니다. %d 부터 %d 사이의 숫자를 입력해주세요: " % (minValue, minValue, maxValue)
    elif comparison > answer:
        maxValue = comparison
        msg = "입력하신 값은 정답보다 큽니다. %d 부터 %d 사이의 숫자를 입력해주세요: " % (minValue, maxValue)
    elif comparison < answer:
        minValue = comparison
        msg = "입력하신 값은 정답보다 작습니다. %d 부터 %d 사이의 숫자를 입력해주세요: " % (minValue, maxValue)
    else:
        print("정답입니다.")
        break

# 2.3 continue
print("\n[ 2.2 continue ] ──────────────────────────────────────────────────────────────────────────────────────────\n")

a = 0
while a < 10:
    a = a + 1
    if a % 3 == 0:
        continue
    print(a)

# 잠시, 파이썬에서 들여쓰기가 중요한 두번째. 아래의 예문은 오류는 없지만, 아무것도 출력되지 않음.

a = 0
while a < 10:
    a = a + 1
    if a % 3 == 0:
        continue
        print(a)  # 들여쓰기 때문에, if 문의 실행문으로 인식되며, 실행될 일이 없다.

# 들여쓰기 하나 때문에, 코드의 의미가 완전 달라지므로 이런 점에 주의할 것.


# 2.4 else
print("\n[ 2.4 else ] ──────────────────────────────────────────────────────────────────────────────────────────────\n")

# 독특하게 반복문에 else 문이 존재함.
# 반복문이 정상적으로 종료될 때 실행됨.

i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i 는 이제 6 보다 작지 않습니다.")

# 단, break 를 통해 강제로 반복문을 빠져나갈 경우 else 문은 실행되지 않는다.

i = 1
while i < 6:
    print(i)
    i += 1
    if i % 3 == 0:
        break
else:
    print("반복문이 종료되었습니다.")
