# 파이썬 기초 (+카카오톡 챗봇) 스터디 1주차

# python 제어문

# 기본적으로 python 의 제어문은 C계열 언어에서 괄호나 중괄호가 쓰이는 것과 달리,
# 띄어쓰기나 탭, 줄바꿈으로 이루어지므로, 이에 유의해야 한다.

# 1. if문

# 기본적으로 if ~ else 의 구조로, 참과 거짓의 조건에 따라 실행하는 형태.

a = int(input("숫자 a를 입력하세요.\n"))
b = int(input("숫자 b를 입력하세요.\n"))

if a > b:
    print("\n" + str(a) + " > " + str(b))
    print("a가 b보다 큽니다.")
else:
    print("b가 a보다 큽니다.")

# elif 문

score = int(input("당신의 국어 성적은 몇 점입니까? "))

if score > 90:
    print("당신의 학점은 A 입니다.")
elif score > 80:
    print("당신의 학점은 B 입니다.")
elif score > 70:
    print("당신의 학점은 C 입니다.")
elif score > 60:
    print("당신의 학점은 D 입니다.")
else:
    print("당신의 학점은 F 입니다.")

# 2. for, while 문

# while 문   : 조건문과 많이 활용.
# for 문     : list, set 등의 자료구조와 많이 활용.

# 2.1 while 문

i = 1
while i < 6:
    print(i)
    i += 1

# break
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

# else
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i 가 6 보다 작지 않습니다.")

# do ~ while 문은 존재하지 않으나, 다음과 같이 할 수 있음.

i = 1
while True:
    print(i)
    i += 1
    if i < 6:
        continue
    else:
        break

# 2.2 for 문

# for 문은 python 에서 list 를 비롯한 컬렉션 형태의 자료형들과 함께 많이 활용됨.
# - javaScript 의 for ~ in 문이나 forEach 에 가까운 형태를 기본으로 가짐.

a = [1, 2, 3]

for i in a:
    print(i)

# 문자열도 가능.
for x in "banana":
    print(x)

# 특정한 list 가 없는 경우, range 를 활용함.

for i in range(5):
    print(i)

# C계열 언어에서 기본 for 문과 같은 의미를 지닌 방식.
for i in range(0, 5, 1):
    print(i)

b = {1, 2, 3, 4, 2}

for i in b:
    print(i)

# index 를 활용할 경우
list1 = ["apple", "banana", "cherry"]
for i in range(len(list1)):
    print(list1[i])

# dict 의 경우
student = {
    "name": "홍길동",
    "gender": "남성",
    "age": 20
}
for x, y in student.items():
    print(x, y)

# ☆☆☆
# 축약표현
list1 = ["apple", "banana", "cherry"]

[print(x) for x in list1]

# - python 에서 굉장히 많이 쓰는 표현으로, print(x) 자리에 사용자 정의 함수를 넣어서 활용함.
# - 축약형은 for 문의 결과를 변수에 저장 가능.
b = [x for x in list1]
print(b)

# 축약 표현을 이용한 구구단의 결과값 저장.
result = [str(x) + "*" + str(y) + "=" + str(x * y) for x in range(1, 10) for y in range(1, 10)]
print(result, type(result))
