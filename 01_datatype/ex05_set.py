# 파이썬 기초 (+카카오톡 챗봇) 스터디 1주차

# python 자료형
# 5. 집합 set

# 순서가 없음. (인덱싱 및 정렬 불가.)
# 중복을 허용하지 않음.
# 수학적 개념

# 자료형의 중복을 제거하기 위한 필터 역할로 종종 사용하기도 한다.

# 5.1 생성 방법
print("\n[ 5.1 생성 방법 ] ─────────────────────────────────────────────────────────────────────────────────────────\n")

# 중괄호 { } 대신 소괄호 ( )를 사용.

s1 = {1, 2, 3}
print(s1)

s2 = set("Hello")
print(s2)  # 중복이 제거됨.

# 순서가 없으므로 indexing 으로 값을 꺼내는 것이 불가능.

# print(s2[1])
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'set' object is not subscriptable

# 길이가 길거나, 내부 요소를 알 수 없는 경우, 원하는 값을 지정하여 꺼내려면 list 나 tuple 로 형변환을 해야한다.
# 또한, print 하거나 내부를 확인할 때마다 정렬이 랜덤하게 나타남.


# 5.2 연산
print("\n[ 5.2 연산 ] ──────────────────────────────────────────────────────────────────────────────────────────────\n")

# +, * 연산자가 지원되는 list 처럼, &, |, - 연산자가 지원됨.


# 교집합: & 또는 intersection 함수를 사용.

s1 = {1, 2, 3, 4, 5, 6}
s2 = set([4, 5, 6, 7, 8, 9])

print(s1 & s2)

print(s1.intersection(s2))

# 합집합: | 또는 union 함수를 사용. 중복해서 포함된 값은 한 개씩만 표현된다.

print(s1 | s2)

print(s1.union(s2))

# 차집합: - 또는 difference 함수를 사용.

print(s1 - s2)

print(s1.difference(s2))


# 5.3 set 관련 함수
print("\n[ 5.3 set 관련 함수 ] ─────────────────────────────────────────────────────────────────────────────────────\n")

"""

* add()         : 집합에 요소를 추가.
* clear()	    : 집합 안의 요소를 모두 제거.
* copy()	    : 집합을 복사하여제공. (*깊은 복사)
* discard()     : 집합에서 해당 요소를 제거함.
* pop()	        : set의 요소 중 하나를 무작위로 꺼내면서 삭제. (list 의 pop() 과 달리 인자가 없음.)
* remove()	    : 특정 값의 요소를 제거. (* discard() 와 달리 해당하는 요소가 없으면 에러 발생.)
* difference()  : 두 집합 혹은 그 이상의 집합에 존재하지 않는 값을 세트로 return. (차집합 개념)
* difference_update() : 현재 집합에 differnce()의 결과를 반영함.
* intersection(): 두 세트 혹은 그 이상의 집합과 공통요소를 세트로 return (교집함 개념)
* intersection_update()	: 현재 집합에 intersection() 결과를 반영함.
* symmetric_difference() : 공통 요소를 제거한 합집합을 세트로 return.
* symmetric_difference_update()	: 현재 집합에 symmetric_difference() 결과를 저장.
* union()	    : 두 집합 혹은 그 이상의 집합의 요소를 모두 집합으로 return. (합집합 개념)
* update()	    : 현재 집합에 union()의 결과를 반영함.
* isdisjoint()  : 공통요소 존재 여부를 return. (공통요소가 없을시 True)
* issubset()	: 모든 요소가 파라미터에도 존재하는지 여부를 return. (부분집합)
* issuperset()  : 파라미터의 모든 요소가 집합에 존재하는지 여부를 return.

"""

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

print("x", x)

print("y", y)

# add()
print("\n# add()")

x.add("orange")

print(x)


# difference()
print("\n# difference()")

print(x.difference(y))
# - 연산자 사용 가능.
print(x - y)

print(x.difference_update(y))  # None
print(x)


# intersection()
print("\n# intersection()")

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

print(x.intersection(y))
# & 연산자 사용 가능.
print(x & y)

x.intersection_update(y)

print(x)


# symmetric_difference()
print("\n# symmetric_difference()")

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

print(x.symmetric_difference(y))

x.symmetric_difference_update(y)

print(x)


# union()
print("\n# union()")

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

print(x.union(y))
# | 연산자 사용 가능.
print(x | y)

x.update(y)

print(x)


# isdisjoint()

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}

print(x.isdisjoint(y))

# issubset(), issuperset()
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}

print(x.issubset(y))
# True
print(y.issuperset(x))
# True


# 5.4 frozenset
print("\n[ 5.4 frozenset ] ─────────────────────────────────────────────────────────────────────────────────────────\n")

# 내부적으로 set 과 동일하지만, tuple 처럼 내부 요소의 변경이 불가능한 집합.

# 자체적인 선언 연산자가 없으며, 형변환을 통해 생성 가능.

set3 = {1, 2, 3, 3, 4, 5, 6, 7}

fs = frozenset(set3)

print(fs, type(fs))

# 내부 함수는 set 의 함수 중 요소를 변경하는 것을 제외하고 동일하게 존재함.

"""
* copy()	    : 집합을 복사하여제공. (*깊은 복사)
* difference()  : 두 집합 혹은 그 이상의 집합에 존재하지 않는 값을 세트로 return. (차집합 개념)
* intersection(): 두 세트 혹은 그 이상의 집합과 공통요소를 세트로 return (교집함 개념)
* symmetric_difference() : 공통 요소를 제거한 합집합을 세트로 return.
* union()	    : 두 집합 혹은 그 이상의 집합의 요소를 모두 집합으로 return. (합집합 개념)
* isdisjoint()  : 공통요소 존재 여부를 return. (공통요소가 없을시 True)
* issubset()	: 모든 요소가 파라미터에도 존재하는지 여부를 return. (부분집합)
* issuperset()  : 파라미터의 모든 요소가 집합에 존재하는지 여부를 return.
"""
