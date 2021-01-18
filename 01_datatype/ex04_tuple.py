# 파이썬 기초 (+카카오톡 챗봇) 스터디 1주차

# python 자료형
# Sequence 형

# list      : 리스트
# tuple     : 튜플
# range     : 범위

# ※ 이 중, list 와 tuple 에 대해서만 따로 다루고 range 는 별도로 다룸.

# 4. 튜플 tuple

# 리스트와 거의 동일하지만, 최초 선언 이후 값을 추가, 수정, 삭제가 불가능한 자료형으로, 변경되지 않아야 할 경우에 활용됨.

# 순서를 가짐. (단, 정렬 및 순서 변경이 불가능.)
# 내부 요소의 중복을 허용함.
# 내부 요소의 추가, 수정, 삭제 등이 불가능.

# 4.1 생성 방법
print("\n[ 4.1 생성 방법 ] ─────────────────────────────────────────────────────────────────────────────────────────\n")

# 리스트와 거의 동일하나, 대괄호 [ ] 대신 소괄호 ( )를 사용.

a = (1, 2, 3, 4, 5)
b = tuple()

print(a, type(a))
print(b, type(b))

# 값의 집적적인 변경이 불가능.

# a[0] = -1
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'tuple' object does not support item assignment


# 일반적으로 list ↔ tuple 변환하여 많이 활용.

c = list(a)

c[0] = -1

print(c)


# 4.2 값 변경 및 연산
print("\n[ 4.2 값 변경 및 연산 ] ───────────────────────────────────────────────────────────────────────────────────\n")

# 튜플의 경우, 직접적으로 요소의 변경이 불가능하므로, list 로 형변환 후
# 값을 추가, 변경, 삭제한 뒤 다시 튜플로 형변환 하는 방법으로 수정이 가능.

a = (1, 2, 3, 4, 5)
temp = list(a)

print(temp)

temp[2] = 100
a = tuple(temp)

print(a)


# 저장된 튜플 자체는 수정이 불가능하지만, 튜플끼리 연산 결과는 새로운 튜플로 return 하므로 리스트와 동일하게 가능.

print((1, 2, 'a', 'b') + (3, 4))

print((1, 2, 'a', 'b') * 2)


# 리스트와 동일하게 slicing 이 가능하지만, 직접적인 변경은 불가능.

a = (1, 2, 3, 4, 5)

print(a[0])
print(a[-1])

print(a[2:])

print( a[-2:])

print(a[1:-2])

print(a[:-2])

print(a[:])

# 이중 배열 구조
a = (1, 2, ['a', 'b', 'c'], 4)

print(a[2][0])


# 4.3 tuple 관련 함수
print("\n[ 4.3 tuple 관련 함수 ] ───────────────────────────────────────────────────────────────────────────────────\n")

"""

* count()	    : 리스트에 해당 요소가 몇 개 포함되어 있는지 체크
* index()	    : 해당 요소가 몇번째에 위치하는지 표시.

"""

# 튜플에는 기본적으로 변경 불가한 자료형이므로, list 에 존재하는 많은 함수들이 없음.

fruits = ('apple', 'banana', 'banana', 'orange')

print("fruits", fruits)


# count()
print("\n# count()")

print(fruits.count("grape"))

# index()
print("\n# index()")

print(fruits.index("banana"))

# list 의 내장 함수와 다르지 않으므로 큰 의미는 없음.
