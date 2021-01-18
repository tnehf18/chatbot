# 파이썬 기초 (+카카오톡 챗봇) 스터디 1주차

# python 자료형
# 2. 숫자형

# int       : 정수형
# float     : 실수형
# complex   : 복소수 ex) 1 + 1j|

# 2.1 생성 방법
print("\n[ 2.1 생성 방법 ] ─────────────────────────────────────────────────────────────────────────────────────────\n")

# - 기본적으로 소수점이 없는 숫자는 기본적으로 int형
a = 123
b = -178
c = 0

# ※ Python에서는 C계열 언어에서 발생하는 int형 자료의 오버플로우가 없음.

#   C계열 언어의 int형 자료의 범위 - 2, 147, 483, 648 ~ 2, 147, 483, 647 -> Long 타입이 별도 존재.
#   Python 2.x에서는 int형에서 오버플로우가 발생하면 자동으로 Long 타입으로 전환되도록 되었으나,
#   Python 3.x 부터는 Long 형이 완전사라지고, int형에서도 arbitrary precision 을 지원하여 통합됨.
#   그러나, 특정 패키지 혹은 라이브러리 사용시에는 여전히 오버플로우가 발생할 수 있음을 주의해야 함.

howlong = 5000000000000

print(howlong, type(howlong))

# 실수형

a = 1.2
b = -3.45

print(type(a))

# 지수 표현식

a = 4.24E10
b = 4.24e-10

print(type(a))


# 2.2 연산
print("\n[ 2.2 연산 ] ──────────────────────────────────────────────────────────────────────────────────────────────\n")

# +     : 덧셈
# -     : 뺄셈
# *     : 곱셈
# **    : 거듭제곱
# /     : 나눗셈(실수형)
# //    : 나눈 몫(정수형)
# %     : 나눈 이후 나머지

# - C계열 언어에서 정수와 정수의 연산은 결과도 정수로만 나타났으나(컴파일 언어시 타입이 지정되기 때문),
# Python 에서는 결과가 실수이면 실수로 처리된다.

print(2.2 * 5)

print(1.0 / .2)

print(3 / 2)

print(type(3 / 2))

print(2 + 5)
print(5 - 1.2)
print(10.2 * 5)
print(2 ** 10)
print(2 ** 10.0)
print(20 / 3)
print(20 // 3.0)
print(20 % 3)
