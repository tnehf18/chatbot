# 파이썬 기초 (+카카오톡 챗봇) 스터디 1주차

# python 자료형
# Sequence 형

# list      : 리스트
# tuple     : 튜플
# range     : 범위

# ※ 이 중, list 와 tuple 에 대해서만 따로 다루고 range 는 별도로 다룸.

# 3. 리스트 list

# Java 나 C계열 언어의 경우, 배열 또는 List 에 해당하며, 그보다는 제약이 적고 굉장히 유연하게 동작함.
# 또한, 제어문이나 표현방식, 선언시 값 대입 등 문법이 C계열 언어와는 달라 숙련도에 따라 활용성이 크게 달라짐.

# 3.1 생성 방법
print("\n[ 3.1 생성 방법 ] ─────────────────────────────────────────────────────────────────────────────────────────\n")

# 대괄호 [ ]를 사용 또는 list()로 생성

list1 = [1, 2, 3, 4, 5]
list2 = list()

print(list1, type(list1))
print(list2, type(list2))

fruits = ['사과', '바나나', '체리']
print(fruits)

# 리스트 내부의 요소는 자료형이 고정되지 않고, 다양한 자료형 가능.

values = [1, 2, '바나나', '사과']
print(values)

values = [1, 2, ['사과', '바나나']]
print(values)


# 3.2 Indexing, Slicing
print("\n[ 3.2 Indexing, Slicing ] ──────────────────────────────────────────────────────────────────────────────────\n")

# 0부터 시작하며, 0 이하의 음수도 입력이 가능. (뒤에서부터 시작함.)
# 콜론(:) 을 이용하여, 범위를 지정 가능.

a = [1, 2, 3, 4, 5]

print(a[0])
print(a[-1])

print(a[2:])

print( a[-2:])

print(a[1:-2])

print(a[:-2])

print(a[:])

# 이중 배열 구조
a = [1, 2, 3, ['a', 'b', 'c']]

print(a[-1][0])


# 3.3 Unpacking
print("\n[ 3.3 Unpacking ] ─────────────────────────────────────────────────────────────────────────────────────────\n")

# 다수의 변수의 값에 list 로 선언시, list 안의 요소로 자동 할당함.

numbers = [1, 2, 3]
a, b, c = numbers

print(a)
print(b)
print(c)

# 변수가 부족할 경우, 에러 발생

# a, b = numbers
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: too many values to unpack (expected 2)

# 이 마저도 * 를 명시하면 변수가 부족해도 자동으로 할당됨.

numbers = [1, 2, 3, 4, 5]
a, b, *c = numbers

print(a)
print(b)
print(c)


# 3.4 연산 및 키워드
print("\n[ 3.4 연산 및 키워드 ] ────────────────────────────────────────────────────────────────────────────────────\n")

# list 에는 +, *의 연산이 지원됨.

# + 더하기

print([1, 2, 3] + [3, 4, 5])

# * 곱하기 (※ 문자열처럼 반복함.)

print([1, 2, 3] * 3)

# in: 특정 요소 포함 여부를 확인.(not 키워드 가능.)

a = ["apple", "banana", "cherry", "orange"]

print("apple" in a)

print("melon" not in a)

#  del: 리스트 안의 특정 요소값을 삭제.

a = ["apple", "banana", "cherry", "orange"]

del a[0]

print(a)

a = [1, 2, 3, 4, 5]

del a[2:]
print(a)


# 3.5 list 관련 함수
print("\n[ 3.5 list 관련 함수 ] ──────────────────────────────────────────────────────────────────────────────────\n")

"""

* append()      : 리스트 마지막에 요소를 추가.
* clear()       : 리스트 안의 요소를 모두 제거.
* copy()        : 리스트를 복사하여 제공. (* 깊은 복사)
* count()	    : 리스트에 해당 요소가 몇 개 포함되어 있는지 체크
* extend()      : 리스트에 리스트(혹은 추가 가능한 요소를)를 뒤에 추가하여 확장.(+ 연산자 가능)
* index()	    : 해당 요소가 몇번째에 위치하는지 표시.
* insert()      : 특정 위치에 해당 요소를 삽입 또는 교체.
* pop()	        : 맨 마지막 요소(인자 없을시) or 특정 위치의 요소를 꺼내면서 삭제.
* remove()      : 특정 값의 요소를 제거. (* 위치로 삭제할 경우, del 키워드 사용가능.)
* reverse()     : 순서를 역전시킴.
* sort()        : 리스트의 요소들을 정렬함 (기본값: 오름차순, 내림차순 및 특정함수 결과 순으로 정렬 가능)

"""

values1 = ["사과", "바나나", "오렌지"]

values2 = ["라면", "떡볶이", "김말이"]

print("values1", values1)
print("values2", values2)

# append()
print("\n# append()")

values1.append("라면")
print(values1)


# copy()
print("\n# copy()")

values3 = values1.copy()


# clear()
print("\n# clear()")

values1.clear()

print(values1)
print(len(values1))

values1 = values3

print(values1)


# count()
print("\n# count()")

print(values2.count("라면"))


# extend()
print("\n# extend()")

print(values1.extend(values2))  # 실행만 하고 return 하지 않으므로 print 결과가 None 으로 나타남.
print(values1)

print(values1.count("라면"))


# index()
print("\n# extend()")

print(values1.index("라면"))  # 처음 확인된 위치만 return.
# print(values1.index("짬뽕"))  # Java 나 C계열 언어와 달리 해당하는 요소가 없으면 에러가 발생함.


# insert()
print("\n# insert()")

values1.insert(6, "만두")
print(values1)


# remove()
print("\n# remove()")

values1.remove("라면")
print(values1)


# reverse()
print("\n# reverse()")

values1.reverse()
print(values1)


# sort()
print("\n# sort()")

values1.sort()
print(values1)

values1.sort(reverse=True)
print(values1)
