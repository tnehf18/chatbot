# 파이썬 기초 (+카카오톡 챗봇) 스터디 3주차

# python 예외처리
# 1. try ~ except

# 1.1 기본 형태
print("\n[ 1.1 기본 형태 ] ─────────────────────────────────────────────────────────────────────────────────────────\n")


def check_even(number):
    if number % 2 == 0:
        print(str(number) + "는 짝수입니다.")
    elif number % 2 == 1:
        print(str(number) + "는 홀수입니다.")
    else:
        print("짝수와 홀수의 판별유무는 2로 나누어 떨어지거나 아닌 정수입니다. 이상한 걸 입력하지 마세요.")


# check_even('메롱')
# TypeError: not all arguments converted during string formatting

try:
    print(1 / 0)
except Exception:
    print("예외가 발생했습니다.")


# 1.2 다양한 형태
print("\n[ 1.2 다양한 형태 ] ───────────────────────────────────────────────────────────────────────────────────────\n")


# 모든 예외 (Exception 생략)
print("\n# 모든 예외 (Exception 생략)")

try:
    print(1 / 0)
except:
    print("예외가 발생했습니다.")


# 다양한 에러 유형에 각각 대처
print("\n# 다양한 에러 유형에 각각 대처")

try:
    print(1 / 0)
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except:
    print("예외가 발생했습니다.")

# 튜플로 하나의 except 문에 활용 가능.

try:
    print(x)
except (ZeroDivisionError, NameError, AttributeError):
    print("에러가 발생했습니다.")


# 리스트로는 불가능.

# try:
#     print(x)
# except [ZeroDivisionError, NameError, AttributeError]:
#     print("에러가 발생했습니다.")

# TypeError: catching classes that do not inherit from BaseException is not allowed


# as 키워드
print("\n# as 키워드")

try:
    print(1 / 0)
except Exception as e:
    print(e.args)


# 1.4 else
print("\n[ 1.4 else ] ──────────────────────────────────────────────────────────────────────────────────────────────\n")

# 예외가 발생하지 않았을 경우, try 문 안의 코드를 실행하고 난 뒤에 실행되는 코드

name = "홍길동"
try:
    print(f"내 이름은 {name}입니다.")
except:
    print("예외가 발생했습니다.")
else:
    print("반갑습니다.")


# 예외가 발생했을 경우에는 실행되지 않음.

del name  # name 변수 삭제

try:
    print(f"내 이름은 {name}입니다.")
except:
    print("예외가 발생했습니다.")
else:
    print("반갑습니다.")


# 1.5 finally
print("\n[ 1.5 finally ] ───────────────────────────────────────────────────────────────────────────────────────────\n")


a = (1, 2, 3, 4, 5)

try:
    a[5] = 6
except Exception as e:
    print("예외가 발생했습니다.", str(e))
finally:
    print("try 문의 수행이 종료되었습니다.")

