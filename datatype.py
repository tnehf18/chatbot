# 파이썬 기초 (+카카오톡 챗봇) 스터디 1주차

# python 자료형

# * 기본적으로 Python은 인터프리터 언어로, C, C  # , C++, Java와 같은 타입형 자료형을 컴파일 시 지정하는 정적언어가 아니라 실행시 결정되는 동적언어이므로,
# 변수 선언시 타입을 명시할 필요가 없는 등 비교적 형변환에서 유동적이다.

# 자료형

# Text Type     : str
# Numeric Types : int, float, complex
# Sequence Types: list, tuple, range
# Mapping Type  : dict
# Set Types     : set, frozenset
# Boolean Type  : bool
# Binary Types  : bytes, bytearray, memoryview

# * Python에서 날짜는 자료형으로 존재하지 않고, time, datetime 등 여러 내장 모듈(패키지)에서 각종 포맷을 제공함.


# 1. 숫자형

# int       : 정수형
# float     : 실수형
# complex   : 복소수 ex) 1 + 1j

# - 기본적으로 소수점이 없는 숫자는 기본적으로 int형

# ※ Python에서는 C계열 언어에서 발생하는 int형 자료의 오버플로우가 없음.
#   C계열 언어의 int형 자료의 범위 - 2, 147, 483, 648 ~ 2, 147, 483, 647 -> Long 타입이 별도 존재.
#   Python 2.x에서는 int형에서 오버플로우가 발생하면 자동으로 Long 타입으로 전환되도록 되었으나,
#   Python 3.x 부터는 Long 형이 완전사라지고, int형에서도 arbitrary precision 을 지원하여 통합됨.
#   그러나, 특정 패키지 혹은 라이브러리 사용시에는 여전히 오버플로우가 발생할 수 있음을 주의해야 함.

# - C계열 언어에서 정수와 정수의 연산은 결과도 정수로만 나타났으나(컴파일 언어시 타입이 지정되기 때문),
# Python에서는 결과가 실수이면 실수로 처리된다.


print(2.2 * 5)
# 11.0

print(1.0 / .2)
# 5.0

print(3 / 2)
# 1.5


# 1.1 연산자

# +     : 덧셈
# -     : 뺄셈
# *     : 곱셈
# **    : 거듭제곱
# /     : 나눗셈(실수형)
# //    : 나눈 몫(정수형)
# %     : 나눈 이후 나머지


# 덧셈
print(2.2 + 5)
# 7.2

# 뻿셈
print(5 - 1.2)
# 8.8

# 곱셈
print(3 * 2)
# 6

print(3.0 * 2)
# 6.0

print(2 ** 10)
# 1024

print(2 ** 10.0)
# 1024.0

# 나눗셈
print(20 / 3)
# 6.666666666666667

print(18 / 3.0)
# 6.0

print(3.2 / 2)
# 1.6

print(20 // 3)
# 6

print(20 // 3.0)
# 6.0

print(20 % 3)
# 2

print(20 % 3.0)
# 2.0


# 2. 문자열

# str: 문자열

# - 기본적으로 C계열에서의 char 타입과 String 구분없이 모두 str로 통일.
# - 단, Python만의 독특한 문자열 표현이 존재.

msg1 = '파이썬 자료형을 학습중입니다.'

msg2 = "파이썬 자료형을 학습중입니다."

print(msg1, type(msg1))

print(msg2, type(msg2))

# * 위 두 결과는 동일하므로, javaScript 처럼 작은 따옴표와 큰 따옴표를 활용 가능.
#    ex) "It's a fine day.", 'He said loudly, "The end will comes".'

# - 멀티라인 문자열 표현(줄바꿈 포함문자열)
# - '''문자열(줄바꿈 포함)''' ("""문자열(줄바꿈 포함)""" ☆ 동일함.)


msg3 = '''아무개님께,

    이 편지는 영국에서 최초로 시작되어 일년에 한 바퀴 돌면서 받는 사람에게 행운을 주었고
    지금은 당신에게로 옮겨진 이 편지는 4일 안에...'''

print(msg3, type(msg3))

# * "아무개님께,\n\n이 편지는 영국에서 최초로 시작되어 일년에 한 바퀴 돌면서 받는 사람에게 행운을 주었고\n지금은 당신에게로 옮겨진 이 편지는 4일 안에..."
# 이 결과와 동일함.

msg4 = "아무개님께,\n\n이 편지는 영국에서 최초로 시작되어 일년에 한 바퀴 돌면서 받는 사람에게 행운을 주었고\n지금은 당신에게로 옮겨진 이 편지는 4일 안에..."

print(msg4, type(msg4), msg3 == msg4)

# 2.1 문자열 연산

# - + 가능.

str1 = "Python"
str2 = " is fun!"

print(str1 + str2)
# 'Python is fun!'


# * (곱셈) 존재.

str1 = "Python"

print(str1 * 3)
# PythonPythonPython


# in: 특정 문자열 포함 여부를 return

str3 = "나는 자유다!"
print("자유" in str3)

# * 이 외 len(str1), split(str1) 등 문자열 함수에 대해서는 추후에 다룰 예정.


# 3. Sequence 형

# list      : 리스트
# tuple     : 튜플
# range     : 범위

# ☆☆☆
# 3.1 list 리스트

# - 대괄호 [] 로 표현.
# - Java나 C계열 언어의 경우, 배열 or List에 해당하며, 그보다는 제약이 적고 굉장히 유연하게 동작함.
# - 또한, 제어문이나 표현방식, 선언시 값 대입 등 문법이 C계열과는 달라 숙련도에 따라 활용성이 크게 달라짐.


numbers = [1, 2, 3, 4, 5]

print(numbers, type(numbers))
# [1, 2, 3, 4, 5]


# - 리스트 내부의 자료형에 대해서 자유로움.

values = [0, "문자열", 3, "파이썬", 5]

print(values, type(values))
# [0, '문자열', 3, '파이썬', 5]

# - 시작은 C계열 언어와 동일하게 0 부터 시작.

print(values[0])

# - 0 이하의 값 입력이 가능함.(뒤에서부터, 단, 시작 위치에 주의.)

# - list의 인덱싱 및 슬라이싱

values = [0, "문자열", 3, "파이썬", 5]

print(values[-1])  # -> 해당 위치의 값을 return
# 5

print(values[2:])  # -> [2] 부터 끝까지 잘라서 list로 return
# [3, '파이썬', 5]

print(values[-2:])  # -> [-2] 부터 끝까지
# ['파이썬', 5]

print(values[1:-2])  # -> [1] 부터 [-2]까지 잘라서 list로 return
# ['문자열', 3]

print(values[:-2])  # -> 처음부터[-2]까지
# [0, '문자열', 3]


# - list 관련 메소드

# append()      : 리스트 마지막에 요소를 추가.
# clear()       : 리스트 안의 요소를 모두 제거.
# copy()        : 리스트를 복사하여 제공. (* 깊은 복사)
# count()	    : 리스트에 해당 요소가 몇 개 포함되어 있는지 체크
# extend()      : 리스트에 리스트(혹은 추가 가능한 요소를)를 뒤에 추가하여 확장.(+ 연산자가 가능)
# index()	    : 해당 요소가 몇번째에 위치하는지 표시.
# insert()      : 특정 위치에 해당 요소를 삽입 또는 교체.
# pop()	        : 맨 마지막 요소(인자 없을시) or 특정 위치의 요소를 꺼내면서 삭제.
# remove()      : 특정 값의 요소를 제거. (* 위치로 삭제할 경우, del 키워드 사용가능.)
# reverse()     : 순서를 역전시킴.
# sort()        : 리스트의 요소들을 정렬함 (기본값: 오름차순, 내림차순 및 특정함수 결과 순으로 정렬 가능)


values1 = ["사과", "바나나", "오렌지"]

values2 = ["라면", "떡볶이", "김말이"]

# append()
values1.append("라면")
print(values1)

# copy()
values3 = values1.copy()

# clear()
values1.clear()
print(values1)
print(len(values1))

values1 = values3

print(values1)

# count()
print(values2.count("라면"))

# extend()
print(values1.extend(values2))  # -> 실행만 하고 return하지 않는 타입이 print 결과가 none으로 나타남.
print(values1)

print(values1.count("라면"))

# index()
print(values1.index("라면"))  # -> 처음 확인된 위치만 return

# insert()
values1.insert(6, "만두")
print(values1)

# remove()
values1.remove("라면")
print(values1)

# reserve()
values1.reverse()
print(values1)

# sort()
values1.sort()
print(values1)

values1.sort(reverse=True)
print(values1)

# list 리스트의 Unpack 하기
# 변수 선언시 변수 값을 list 로 선언할 경우, 자동으로 해당 list의 길이만큼 순서대로 값이 할당된다.
values2 = [2, 3, 5]

a, b, c = values2
print(a)
print(b)
print(c)

a, b = values2
# 변수 수가 list 의 길이에 비해 부족할 경우 에러 발생. too many values to unpack (expected 2)
# 단, *를 활용하면 변수가 부족할 경우에도 할당이 가능함.

fruits = ["apple", "banana", "cherry", "strawberry", "raspberry"]

green, yellow, *red = fruits

print(green)
print(yellow)
print(red)

[green, yellow, *red] = fruits

print(green)
print(yellow)
print(red)

values = [green, yellow, *red] = fruits

print(values[0])
print(yellow)
print(red)

print(values)
print(len(values))

# * 이렇게도 가능하나, 이를 헷갈려하지 말 것, 변수 values 에는 최종적으로 그냥 fruits가 삽입됐다고 이해하는 게 맞음.
# a, b = 2 이런 식으로 values 와 [green, yellow, *red] 에 fruits 가 각각 삽입됐다고 이해하는 것이 옳으나,
# 정작, values, [green, yellow, *red] = fruits 라고 코드를 작성하면 변수가 부족하다고 에러가 발생함. (이를 이해하는 것이 중요.)

# + 연산자 활용 가능. (* extend() 함수 대체 가능.)
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# 3.2 tuple 튜플

# - 괄호 ()로 표현.
# - list와 동일한 형태의 자료구조 형태이나, 한번 선언되면, 내부 요소의 추가/변경/삭제가 불가능.
# - 변경되지 않아야 할 자료를 담을 때 활용. (* 실질적으로는 대부분 list가 더 많이 활용됨.)


numbers2 = (1, 2, 3, 4, 5)

print(type(numbers2))
print(numbers2)

numbers2.append(6)
# 에러 발생. tuple 에는 append 속성이 없다고 함.
# 마찬가지로, count(), index(), len() 정도의 함수만 있고, list 에서 사용하는 다수의 함수들이 tuple에 존재하지 않음.
# 단, 자료구조 형태는 같으므로, 값을 변경해야 할 경우, list 형변환을 통해 변경하는 것을 권장하고 있음.

temp = list(numbers2)
temp.append(6)
number2 = tuple(temp)

print(number2)

# 3.3 range

# range 는 별도의 자료형으로 존재하나, collection 형태의 자료구조와는 거리가 멀고 순수하게 범위를 뜻함.
# for 문 등의 반복문에 주로 활용됨.

a = range(2, 6)

print(a)
print(type(a))

print(list(a))

# range(start, stop, step) 으로 설정시 혹은, 속성값으로 간격 설정 가능.

a = range(2, 10, 2)

print(list(a))

# range 의 속성값들은 모두 readonly 로 변경이 불가.


# 4. Set

# set       : 정수형
# frozenset : 실수형

# 4.1 set

# - 중괄호 {}로 표현.
# - list 와 달리 순서가 존재하지 않고(정렬 불가), 요소의 중복을 허용하지 않음.
# - 수학의 집합의 개념으로 여김.

# - set 관련 메소드

# add()         : 세트에 요소를 추가.
# clear()	    : 세트 안의 요소를 모두 제거.
# copy()	    : 세트를 복사하여제공. (*깊은 복사)
# discard()     : 세트에서 해당 요소를 제거함.
# pop()	        : set의 요소 중 하나를 무작위로 꺼내면서 삭제. (list 의 pop() 과 달리 인자가 없음.)
# remove()	    : 특정 값의 요소를 제거. (* discard() 와 달리 해당하는 요소가 없으면 에러 발생.)
# difference()  : 두 세트 혹은 그 이상의 세트에 존재하지 않는 값을 세트로 return. (차집합 개념)
# difference_update() : 현재 세트에 differnce()의 결과를 반영함.
# intersection(): 두 세트 혹은 그 이상의 세트와 공통요소를 세트로 return (교집함 개념)
# intersection_update()	: 현재 세트에 ntersection() 결과를 반영함.
# symmetric_difference() : 공통 요소를 제거한 합집합을 세트로 return.
# symmetric_difference_update()	: 현재 세트에 symmetric_difference() 결과를 저장.
# union()	    : 두 세트 혹은 그 이상의 세트의 요소를 모두 세트로 return. (합집합 개념)
# update()	    : 현재 세트에 union()의 결과를 반영함.
# isdisjoint()  : 공통요소 존재 여부를 return. (공통요소가 없을시 True)
# issubset()	: 모든 요소가 파라미터에도 존재하는지 여부를 return. (부분집합)
# issuperset()  : 파라미터의 모든 요소가 세트에 존재하는지 여부를 return.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

# add()
x.add("orange")

print(x)
# {"apple", "banana", "cherry", "orange"}

# difference()
print(x.difference(y))
# {'banana', 'orange', 'cherry'}

# - 연산자 사용 가능.
print(x - y)

print(x.difference_update(y))
# None
print(x)
# {'cherry', 'orange', 'banana'}

# intersection()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

print(x.intersection(y))
# {"apple"}

# & 연산자 사용 가능.
print(x & y)

x.intersection_update(y)

print(x)
# {"apple"}

# symmetric_difference()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

print(x.symmetric_difference(y))
# {'google', 'banana', 'microsoft', 'cherry'}

x.symmetric_difference_update(y)

print(x)
# {'google', 'banana', 'microsoft', 'cherry'}


# union()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

print(x.union(y))
# {'google', 'banana', 'apple', 'microsoft', 'cherry'}

# | 연산자 사용 가능. (* + 연산자는 list 에만 지원됨.)
print(x | y)

x.update(y)

print(x)
# {'google', 'banana', 'apple', 'microsoft', 'cherry'}


# isdisjoint()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}

print(x.isdisjoint(y))
# True

# issubset(), issuperset()
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}

print(x.issubset(y))
# True
print(y.issuperset(x))
# True


# 4.2 frozenset

# - tuple 처럼, 형태는 set와 동일하나, 요소의 추가, 변경, 삭제가 불가능함.
# - update에 해당하는 함수들이 존재하지 않음.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = frozenset(x)

print(z, type(z))

# frozenset 에 다른 set을 합친 결과는 frozenset이 됨.
print(z | y)

# 5. 매핑형

# dict: 딕셔너리

# - C계열 언어의 Map처럼 Key와 Value로 구성되 자료형.
# - {}로 선언하며, 순서는 지정되지 않은 Key의 중복을 허용하지 않음.
# - Key 로 list 나 set 등의 컬렉션 형태의 자료형은 사용할 수 없다.

dict1 = {
    1: "Ford",
    "model": "Mustang",
    "year": 1964,
    None: None
}

print(dict1)
# {1: 'Ford', 'model': 'Mustang', 'year': 1964, None: None}

# - 딕셔너리 요소 꺼내기
print(dict1["model"])
# "Mustang"
print(dict1.get("model"))
# "Mustang"

# keys() 함수를 사용하면, 키들을 list 로 return.

print(dict1.keys(), type(dict1.keys()))
# type 명이 dict_keys 라고 나오지만, []로 표현된 걸 보면, list의 하위 class 임을 알 수 있다.

# - 딕셔너리 관련 메소드

# clear()	    : 딕셔너리 안의 요소를 모두 제거.
# copy()	    : 딕셔너리를 복사하여 제공. (*깊은 복사)
# fromkeys()	: 키와 값으로 묶어 딕셔너리로 return.
# get()	        : 딕셔너리에서 해당하는 키로 값을 return.
# items()	    : 키와 값을 한 쌍으로 튜플로 묶어, list로 return. (* 단순히, value만 return 되는 것이 아님에 주의.)
# keys()	    : 키들을 list로 return.
# values()	    : 값들을 list로 return.
# pop()	        : 딕셔너리에서 키에 해당하는 값을 return. (인자로 키 필수.)
# popitem()	    : 마지막에 입력된 key 요소를 제거.
# setdefault()	: 딕셔너리에 해당 key 와 value 를 추가하고 value 값을 return. 단, 이미 key가 있는 경우, 기존 키의 값을 return만 함.
# update()	    : 딕셔너리에 해당 key 와 value 를 추가하거나 해당 키의 값을 바꿈. (* 인자로 dict 형태로 넣어야 함.)


# 6. bool

# - 참 or 거짓을 나타내는 자료형.
# - True, False 모두 대문자 값만을 가짐.(", ' 등의 따옴표 없이 입력)
# - 다른 자료형의 값에 따라 참과 거짓을 구별하기도 한다.

#     값     Ture or False
#  "문자열"     True
#  ""           False
#  [1, 2, 3]    True
#  []           False
#  ()           False
#  {}           False
#  1(*0 이 아닌 모든 숫자) True
#  0            False
#  None         False


a = True

print(a)

print(bool("이것은 공백 문자가 아닙니다."))
print(bool(""))
print(bool([]))
print(bool(()))
print(bool({}))

b = bool(6)
print(b)
print(int(b))
print(bool(0))
