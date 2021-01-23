# 파이썬 기초 (+카카오톡 챗봇) 스터디 2주차

# python 함수
# 1. 기본 구조

# 1.1 생성 및 호출
print("\n[ 1.1 생성 및 호출 ] ─────────────────────────────────────────────────────────────────────────────────────────\n")


def calc_area(width, height):
    return width * height


print(calc_area(10, 20))

# 재사용 가능.
print(calc_area(12, 3.33))

# 1.2 인자와 반환여부에 따른 형태
print("\n[ 1.2 인자와 반환여부에 따른 형태 ] ───────────────────────────────────────────────────────────────────────\n")

# return 생략
print("\n# return 생략")


def check_even(number):
    if number % 2 == 0:
        print(str(number) + "는 짝수입니다.")
    elif number % 2 == 1:
        print(str(number) + "는 홀수입니다.")


check_even(4)

# return 포함
print("\n# return 포함")


def check_even2(number):
    result = False
    if number % 2 == 0:
        result = True
        print(str(number) + "는 짝수입니다.")
    elif number % 2 == 1:
        print(str(number) + "는 홀수입니다.")
    return result


a = check_even2(9)
print(a)

# return 으로 함수 빠져나가기
print("\n# return 으로 함수 빠져나가기")


def escape():
    print("1번 말이 달립니다.")
    print("2번 말이 달립니다.")
    print("3번 말이 달립니다.")
    return
    print("4번 말이 달립니다.")  # 실행되지 않음.
    print("5번 말이 달립니다.")


escape()

# 1.3 매개변수와 인자
print("\n[ 1.3 매개변수와 인자 ] ───────────────────────────────────────────────────────────────────────────────────\n")


# 매개변수 (parameter): 함수에서 필요로 하는 데이터를 가리키는 변수. (=인자)
# 인수 (argument): 함수 호출시 변수에 전달되는 값.

def calc_area(width, height):  # 매개변수: width, height
    return width * height


calc_area(10, 20)  # 인수: 10, 20

print('''
>>> calc_area(10, 20)
매개변수: width, height
인수 : 10, 20
''')

# 매개변수가 필요로 하는 함수에, 인수를 넣지 않을 경우.

# calc_area()
# Traceback(most recent call last):
#   File "<stdin>", line 1, in < module >
# TypeError: calc_area() missing 2 required positional arguments: 'width' and 'height'


# 매개변수가 존지하지 않은 함수
print("\n# 매개변수가 존재하지 않은 함수")


def beep():
    print("빵빵")


beep()

# 매개변수가 일정하지 않은 경우

# 매개변수에 기본값이 존재
print("\n# 매개변수에 기본값이 존재")


def square(r, p=2):
    return r ** p


print(square(2))
print(square(2, 10))


# Tip. 필수 인자가 아닌 p 는, 필수 인자인 r 보다 오른쪽에 인자로 선언되어야 함.

# def square(p=2, r):  # -> 함수 선언 자체가 불가능.
#     return r ** p

# ※ python 의 오버로딩.
# Java 나 C계열 언어의 오버로딩(Overloading)과 비슷하게 사용하는 느낌이지만, 호출시 인수만 다를 뿐,
# 함수를 재정의하여 사용하는 것은 아니므로 차이가 있음.

# ※ python 에서 오버로딩이 아예 불가능한 것은 아님.


def sqaure(r, p=3):
    return r ** p


print(square(2))  # p=2
print(sqaure(2))  # p=3

# 그러나, 재정의하여 오버로딩이 가능함에도 불구하고, python 의 언어 특성상, 매개변수에 타입도 명시되지 않고
# 실행하는 문장에서 예외가 발생하지 않는 이상 인수의 타입에 제약도 없으므로, 사용자 입장에서 이게 함수인지 알기 어렵다.
# 따라서, python 에서는 일반적으로 오버로딩 보다는 함수명을 명확하게 명시할 것을 권장하고 있다.

# 또한, 현재 IDE 에서 소스파일 안의 각 함수를 구분하여 인식해주었기에 가능한 일이지,
# 터미널 등의 외부에서 함수를 호출하려고 하면 구분할 길이 없으므로 마지막에 정의된 함수만 불러오게 된다.

# print() 함수의 디폴트 인수: end
print("\n# print() 함수의 디폴트 인수: end")

print("print() 함수의 end 에 기본값이 아닌 인수를 입력합니다", end=": ")

# 입력받을 인수의 개수가 불특정한 경우: * 활용.
print("\n# 입력받을 인수의 개수가 불특정한 경우: *")


def add_all(*args):
    tot = 0
    for i in args:
        tot += i
    return tot


print(add_all(1, 2, 3, 4))
# 10
print(add_all(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
# 55


# 키워드 인수: 함수에 지정된 변수명을 이용하여 인자를 지정하는 방법.
print("\n# 키워드 인수")


def rgb_to_hex(red=0, green=0, blue=0):
    print("#%02x%02x%02x" % (red, green, blue))


rgb_to_hex(blue=204)

# ☆☆☆
# 가변 키워드 인수: ** 로 명시하고, key=value 의 형태로 인수를 입력하여, 딕셔너리 형태로 함수에 전달됨.
print("\n# 가변 키워드 인수")


def open_dict(**knv):
    print(knv, type(knv))


open_dict(name='홍길동', age=20, gender='남성')
open_dict(title='채식주의자', writer='한강')

# 키워드 인수에 key 에는 따옴표(', ")는 사용할 수 없으며, 모두 문자열로 인식한다.
# 또한, 숫자나 True, False 역시 사용할 수 없으며, 키워드 인수의 key 에는 입력할 수 없는 것들이 존재.

# open_dict(1='홍길동')  # 실행 자체가 불가

# open_dict({1: '홍길동'})  # 실행 자체는 가능하지만, 에러 발생.

# Traceback (most recent call last):
#   File "<stdin>", line 1, in < module >
# TypeError: open_dict() takes 0 positional arguments but 1 was given


# 1.4 전역변수와 지역변수
print("\n[ 1.4 전역변수와 지역변수 ] ───────────────────────────────────────────────────────────────────────────────\n")

# 전역변수
print("\n# 전역변수")

glb = 1
print("glb =", glb)


# def access_glb():
#     glb += 1

# Traceback (most recent call last):
#   File "<stdin>", line 1, in < module >
#     access_glb()
#   File "<stdin>", line 1, in access_glb
# UnboundLocalError: local variable 'glb' referenced before assignment

# javaScript 나  달리, 함수 영역 안에서 함수 밖의 변수에 접근하려면 global 키워드로 명시해야만 가능.

def access_glb():
    global glb
    glb += 1


access_glb()
print(glb)

# 지역변수
print("\n# 지역변수")

glb = 1


def access_local(arg):
    arg += 1
    return arg


print(access_local(glb))

# javaScript 의 경우, 전역변수에 아무렇게나 접근할 수 있거나, 지역변수와 구분이 없어서
# 작성자가 함수로 만들었지만, 전역변수를 제어하는 경우 함수를 분리하거나 재활용하기 어렵다.
#
# 특히 onclick 등 이벤트에 사용되는 함수들.
#
# 그런 점에 비해서, global 로 전역변수를 명시하거나, 함부로 함수의 안팎을 제어하지 않도록 구분하는 점은 굉장히 좋아보임.


# 1.5 람다식
print("\n[ 1.5 람다식 ] ────────────────────────────────────────────────────────────────────────────────────────────\n")

'''
  - Java 에서의 람다식 예시

  List<Object> list = new ArrayList<>();
   
  ...
  
  list.forEach(obj -> System.out.println(obj));

  ※ Java 에서는 보통 다른 클래스의 함수를 오버라이딩 하여, 익명함수를 구현. 재사용 불가.


  
  - javaScript 에서의 익명함수 예시
  
  var a = function() {
      //수행할 코드
      alert("익명함수 입니다.");
  }
  //변수를 호출
  a();

  ※ 함수 자체는 새로이 만들어졌지만, 재사용은 가능.
  
  
  - javaScript 에서의 람다식 예시

  var mul = (a, b) => {return a * b};

'''

add = lambda x, y: x + y  # return 명령어가 없어도 결과값을 return.

print(add(2, 5))

# 함수를 간략하게 나타낼 수 있음.

# 하지만, 이렇게 만들거면 람다식을 쓰지말고, def 키워드로 함수로 만들라고 나온다.
# PEP 8: E731 do not assign a lambda expression, use a def

# 익명함수식 표현
print("\n# 익명함수식 표현")

print((lambda x, y: x + y)(2, 5))

# Python 에서는 람다식을 쓸 경우, 인수로 바로 쓰는 것을 권장하고 있다.

# 람다식을 활용하여, sorted() 함수의 인자로 전달.

rev = sorted((lambda x, y: list(range(x, y+1)))(2, 5), reverse=True)
print(rev)
