# 파이썬 기초 (+카카오톡 챗봇) 스터디 1주차

# python 자료형
# 7. bool

# - 참 or 거짓을 나타내는 자료형.
# - True, False 모두 대문자 값만을 가짐.(", ' 등의 따옴표 없이 입력)
# - 다른 자료형의 값에 따라 참과 거짓을 구별하기도 한다.

# 7.1 생성 방법
print("\n[ 7.1 생성 방법 ] ─────────────────────────────────────────────────────────────────────────────────────────\n")

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
