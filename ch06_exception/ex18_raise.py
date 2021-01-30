# 파이썬 기초 (+카카오톡 챗봇) 스터디 3주차

# python 예외처리
# 2. 강제 예외 발생

# 2.1 raise
print("\n[ 2.1 raise ] ─────────────────────────────────────────────────────────────────────────────────────────────\n")

x = "hello"

# if not type(x) is int:
#   raise TypeError("정수형만 입력 가능합니다.")

# Traceback (most recent call last):
#   File "<stdin>", line 2, in <module>
# TypeError: 정수형만 입력 가능합니다.


def check_even(number):
    try:
        if not number.__class__ is int:
            raise TypeError("정수만 입력해주세요.")
    except Exception as e:
        print(str(e))
    else:
        if number % 2 == 0:
            print("%d 는 짝수입니다." % number)
        elif number % 2 == 1:
            print("%d 는 홀수입니다." % number)
    finally:
        print("check_even() 함수가 종료되었습니다.")


check_even("메롱")

check_even(1)


# 2.1 사용자 정의 오류
print("\n[ 2.1 사용자 정의 오류 ] ──────────────────────────────────────────────────────────────────────────────────\n")

# Exception 클래스를 상속받아 사용자 정의 오류 정의 가능.


class MinusNumberError(Exception):

    def __init__(self, msg="0보다 작은 숫자입니다."):
        super().__init__(msg)


x = -10

try:
    if x < 0:
        raise MinusNumberError
except MinusNumberError as me:
    print(str(me))
except:
    print("예외가 발생했습니다.")
else:
    print("x는 0보다 큽니다.")

