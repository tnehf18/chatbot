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
print(student.items())
for x, y in student.items():
    print(x, y)

# ☆☆☆
# 축약표현
list1 = ["apple", "banana", "cherry"]

[print(x) for x in list1]

for x in list1:
    print(x)
# - python 에서 굉장히 많이 쓰는 표현으로, print(x) 자리에 사용자 정의 함수를 넣어서 활용함.
# - 축약형은 for 문의 결과를 변수에 저장 가능.
b = [x for x in list1]
print(b)

# 축약 표현을 이용한 구구단의 결과값 저장.
result = [str(x) + "*" + str(y) + "=" + str(x * y) for x in range(1, 10) for y in range(1, 10)]
print(result, type(result))
