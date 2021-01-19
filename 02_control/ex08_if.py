# 파이썬 기초 (+카카오톡 챗봇) 스터디 1주차

# python 제어문
# 8. 조건문 if

# 8.1 기본 형태
print("\n[ 1.1 기본 형태 ] ─────────────────────────────────────────────────────────────────────────────────────────\n")

# 기본적으로 python 의 제어문은 C계열 언어에서 괄호나 중괄호가 쓰이는 것과 달리,
# 띄어쓰기나 탭, 줄바꿈 등 들여쓰기(indent)에 주의해서 작성해야 한다.

a = 5
b = 12
if a > b:
    print("a가 b 보다 큽니다.")
else:
    print("b가 a 보다 큽니다.")


# 기본적으로 if ~ else 의 구조로, 참과 거짓의 조건에 따라 실행하는 형태.

# C계열 언어나 Java 등의 다른 언어를 먼저 배운 사람들은 조금 적응하기 힘든 부분.
# 개인적으로 들여쓰기에 너무 민감해서 굉장히 번거롭고, 가뜩이나 세미콜론(;)도 잘 안 쓰는데 너무 해괴하게 보임...
# 또한, else 뒤에 콜론(:)을 반드시 붙여야 하는 점도 약간 짜증.

# 리스트 활용시
a = (1, 2, 3, 4)
b = []
if bool(b):
    print("b 는 True 입니다.")
else:
    print("b 는 False 입니다.")


# 굳이 bool 로 캐스팅하지 않아도 인식함.
if []:
    print("생성 되었습니다.")
else:
    print("아무것도 들어있지 않습니다.")


# ※ javaScript 에서 빈 배열은 true 로 인식함으로 이를 조심.

# if ([]) {
#     alert("빈 배열이지만, true 입니다.");
# }
# else {
#     alert("배열 내부는 비었고, false 입니다.");
# }


# 8.2 여러 조건문 실행
print("\n[ 8.2 여러 조건문 실행 ] ──────────────────────────────────────────────────────────────────────────────────\n")

# elif
print("\n# elif")

# if ~ else 만으로 할 경우

score = 84

if score >= 90:
    print("Grade A")
else:
    if score >= 80:
        print("Grade B")
    else:
        if score >= 70:
            print("Grade C")
        else:
            if score >= 60:
                print("Grade D")
            else:
                print("Grade F")

# elif 사용시

if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
elif score >= 60:
    print("Grade D")
else:
    print("Grade F")


# 한 줄로 표현

if score >= 90: print("Grade A")
elif score >= 80: print("Grade B")
elif score >= 70: print("Grade C")
elif score >= 60: print("Grade D")
else: print("Grade F")

# 다만 한 줄로 표현할 경우, 실행문이 길면 각 실행문을 구분하기 위해 세미콜론(;)이 필요해지고, 가독성이 더 떨이질 수 있음.

if score >= 90: print("Grade A")
elif score >= 80: print("Grade B")
elif score >= 70: print("Grade C"); print("재수강입니다.")
elif score >= 60: print("Grade D"); print("재수강입니다.")
else: print("Grade F"); print("재수강입니다.")


# and, or, not
print("\n# and, or, not")

# 이렇게 쓰지 않도록 주의. (&, | 기호 보다 and, or, not 을 권장하는 이유)

if True & True:
    print("참입니다.")
else:
    print("거짓입니다.")


if 100 & True:
    print("참입니다.")
else:
    print("거짓입니다.")

# 여기까지는 가능하나, 아래는 모두 에러가 발생.

# if 1.1 & True:
#     print("참입니다.")
# else:
#     print("거짓입니다.")
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: unsupported operand type(s) for &: 'float' and 'bool'

# if True & [1, 2, 3, 4]:
#     print("참입니다.")
# else:
#     print("거짓입니다.")
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: unsupported operand type(s) for &: 'bool' and 'list'

# if True & "문자열":
#     print("참입니다.")
# else:
#     print("거짓입니다.")
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: unsupported operand type(s) for &: 'bool' and 'str'


# 기본적으로 Python 에서 &, | 연산자는 교집합과 합집합 연산자로 동작한다.

if True and "":
    print("참입니다.")
else:
    print("거짓입니다.")


if False or [1, 2, 3, 4]:
    print("참입니다.")
else:
    print("거짓입니다.")


if not "참":
    print("참입니다.")
else:
    print("거짓입니다.")

# pass : if 문에서 아무것도 실행하지 않고자 할 경우, 사용.

pocket = ['paper', 'money', 'cellphone']

if 'money' in pocket:
    pass
else:
    print("money가 없습니다.")

# if 'money' in pocket:
# else:
#     print("money가 없습니다.")

# Java 나 C계열 언어에서는 실행문이 비어 있어도 그냥 넘어가지만, Python 에서는 에러가 발생하므로, pass 를 명시해야 한다.


# 8.3 다른 표현 방법
print("\n[ 8.3 다른 표현 방법 ] ────────────────────────────────────────────────────────────────────────────────────\n")

# 조건부 표현식
print("\n# 조건부 표현식")

score = int(input("점수를 입력해주세요.\n"))

msg = "success" if score >= 80 else "failure"
print(score, msg)


# is 키워드
print("\n# is 키워드")

# == 비교연산자와 비슷한 is 가 존재하지만, 주의.

a = [1, 2, 3]
b = a           # 삽입되는 값은 a 라는 객체 그 자체이며, 그 개체의 고유한 id 값이 들어감. -> 얕은 복사

if a is b:
    print("같습니다.")
else:
    print("다릅니다.")


c = a.copy()    # a 객체의 값을 복사하여 새로운 객체 c 에 넣음. -> 깊은 복사

if a is c:
    print("같습니다.")
else:
    print("다릅니다.")

# is 는 생성된 변수의 id 값이 같은지 비교함.
# Python 에서 변수의 id 값은 내부 객체 및 생성된 변수를 가리키는 고유한 상수이지만, 메모리 주소는 아님.
