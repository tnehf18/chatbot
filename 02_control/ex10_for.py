# 파이썬 기초 (+카카오톡 챗봇) 스터디 1주차

# python 제어문
# 3. 반복문 for

# 3.1 기본 형태
print("\n[ 3.1 기본 형태 ] ─────────────────────────────────────────────────────────────────────────────────────────\n")

numbers = [1, 2, 3]

print(numbers, type(numbers))

for i in numbers:
    print(i)


# range() 활용
print("\n# range() 활용")

for i in range(0, 5):
    print(i)

for i in range(5):
    print(i)

# C계열 언어에서 기본 for 문과 같은 의미를 지닌 방식.
for i in range(0, 5, 1):
    print(i)


# 3.2 for 문의 응용
print("\n[ 3.2 for 문의 응용 ] ─────────────────────────────────────────────────────────────────────────────────────\n")

# 문자열
print("\n# 문자열")

print("banana", type("banana"))
for c in "banana":
    print(c)

text = "동해물과 백두산이 마르고 닳도록 하느님이 보우하사 우리나라 만세"
print(text, type(text))

for word in text.split():
    print(word)

# index 출력하기. len(), range() 활용
print("\n# index 출력하기. len(), range() 활용")

fruits = ["apple", "banana", "cherry"]
print(fruits, type(fruits))

for i in range(len(fruits)):
    print(i, fruits[i])


# 이중 구조를 가진 경우
print("\n# 이중 구조를 가진 경우")

# 변수가 하나가 아니라 복수로 선언하면 자동으로 각각 변수에 값을 할당하여 반복문을 실행.

coord = [(0, 0), (10, 5), (20, 25)]
print(coord, type(coord))

for x, y in coord:
    print(x, y)

# 변수가 부족하거나 일치하지 않을 경우, 에러가 발생함.

# coord = [(0, 0), (10, 5), (20, 25)]
#
# for x, y, z in coord:
#     print(x, y, z)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: not enough values to unpack (expected 3, got 2)

# coord = [(0, 0, 1), (10, 5, 2), (20, 25, 3)]
#
# for x, y in coord:
#     print(x, y)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: too many values to unpack (expected 2)


# 딕셔너리의 경우
print("\n# 딕셔너리의 경우")

student = {
    "name": "홍길동",
    "gender": "남성",
    "age": 20
}
print(student, type(student))

# keys()
for k in student.keys():
    print(k)

# values()
for v in student.values():
    print(v)

# items()
for k, v in student.items():
    print(k, v)


# 3.3 break, continue, else
print("\n[ 3.3 break, continue, else ] ─────────────────────────────────────────────────────────────────────────────\n")

# while 문과 동일하게 break, continue, else 사용 가능.

fruits = ["apple", "banana", "cherry"]
print(fruits, type(fruits))

# break
for x in fruits:
    print(x)
    if x == "banana":
        break

# continue
for x in fruits:
    if x == "banana":
        continue
    print(x)

# else
for x in fruits:
    print(x)
else:
    print("There are %d kinds of fruits" % len(fruits))


# ☆☆☆
# 3.4 축약표현
print("\n[ 3.3 축약표현 ] ──────────────────────────────────────────────────────────────────────────────────────────\n")

# 대괄호 [ ]로 for 문을 둘러싸서 축약 가능.

fruits = ["apple", "banana", "cherry"]
print(fruits, type(fruits))

[print(x) for x in fruits]

# python 에서 굉장히 많이 쓰는 표현으로, print(x) 자리에 사용자 정의 함수를 넣어서 활용함.
# 축약형은 for 문의 결과를 변수에 저장 가능.
# ()나 {}는 불가능하며, 결과는 list 로 반환된다.

b = [x for x in fruits]

print(b, type(b))

# 축약 표현을 이용한 구구단의 결과값 저장.

result = [str(x) + "*" + str(y) + "=" + str(x * y) for x in range(1, 10) for y in range(1, 10)]
print(result)

# ()는 다르게 캐스팅 되어 사용 불가.
# b = (x for x in fruits)
# print(b, type(b))

# {}는 변수로는 저장 가능하지만, 실행이 되지는 않는다.
{print(x) for x in fruits}

b = {x for x in fruits}
print(b, type(b))
