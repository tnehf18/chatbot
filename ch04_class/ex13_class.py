# 파이썬 기초 (+카카오톡 챗봇) 스터디 2주차

# python 클래스
# 1. 기본 구조

# 1.1 생성 및 호출
print("\n[ 1.1 생성 및 호출 ] ──────────────────────────────────────────────────────────────────────────────────────\n")


class Test:
    pass


obj = Test()

print(obj, type(obj))


# 다른 소스파일의 클래스 호출
print("\n# 다른 소스파일의 클래스 호출")

from classes import Empty


obj2 = Empty()

print(obj2, type(obj2))

'''

# 전통적인 방식 / 타 언어에서의 클래스 생성 방식과 비교. (특히, Java, C계열 등의 컴파일러 언어)

  class 클래스명 {

      //필드
      속성1
      속성2
      ...

      //생성자
      ...

      //메소드
      ...

  }

  컴파일러 언어들은 실행 전에 컴파일되어 작업이 수행되므로, 클래스의 속성이 미리 정의되어야 하는 경우 많음.
  반면, Python 의 특성상, 실행될 때 메모리에 올라가므로 굳이 필드가 미리 정의되어야 할 필요가 없음.
  
  Python 에서 클래스 생성시 new 키워드를 사용하지 않는 것 또한 이런 이유 때문.

'''


class MyClass:
    attr = '속성'


print(MyClass)  # ()를 생략하고 클래스명을 직접 입력하면 타입이 반환됨.
print(MyClass.attr)


'''

Python 에서 타 언어의 방식처럼, 클래스에 필드를 먼저 정의하는 게 불가능한 것은 아님.
 
다만, 굳이 미리 속성이 선언될 필요가 없기 때문에, 일반적으로 생성자에서 바로 정의하는 방식을 많이 사용.

속성에 기본값을 주입하는 것 역시, 함수의 매개변수에 기본값을 지정하는 게 가능하기 때문에,
생성자에 매개변수의 기본값을 입력할 수도 있으므로 생성자 외부에 미리 정의하는 게 큰 의미가 없음.
'''


# 1.2 생성자
print("\n[ 1.2 생성자 ] ────────────────────────────────────────────────────────────────────────────────────────────\n")

from classes import *  # 정의된 모든 클래스 import.


# Human() 객체 생성
print("\n# Human() 객체 생성")

gd = Human('홍길동', 20, '남성')

print(gd.name)


# 클래스에서 언더스코어(_) 활용법 1. 약한 private -> 정확하게는 hiding(은닉)
print("\n# 언더스코어(_) 활용법 1.")

nabi = Cat('나비')

print(nabi.sentence())

# Cat 객체 생성후 객체의 속성에 보이지 않는 것을 확인할 수 있다.
# 그러나, 사용자가 정의된 변수명을 미리 알고 있다면 직접적으로 호출하는 것이 불가능한 것은 아님.

# print(a._internal_kind)  # 출력됨.

# Python 에서 진정한 의미에서 private 기능은 없다고 함.


# 클래스에서 언더스코어(_)) 활용법 2. 충돌(오버라이딩) 방지
print("\n# 언더스코어(__) 활용법 2.")

a = A()

b = B()

print(a.attr1, b.attr1)
print(a.__attr2__, b.__attr2__)

# 서로 같은 이름의 속성을 가지지만 오버라이드가 되지 않는다.


# 생성자의 다형성 구현 방법. (유사 오버로딩)
print("\n# 생성자의 다형성 구현 방법. (유사 오버로딩)")

# 기본 생성자처럼 활용
person1 = Person()

print("\nperson1", person1.__class__)
print(person1.name)
print(person1.age)
print(person1.gender)

person2 = Person('김독자', 28, '남성')

print("\nperson2", person2.__class__)
print(person2.name)
print(person2.age)
print(person2.gender)

student1 = Student(str_to_std="학생1,18,남성")

print("\nstudent1", student1.__class__)
print(student1.name)
print(student1.age)
print(student1.gender)


# 1.3 속성
print("\n[ 1.3 속성 ] ──────────────────────────────────────────────────────────────────────────────────────────────\n")

# 인스턴스 속성: __init__ 에서 self.속성 에 할당 했던 변수들은 모두 인스턴스 속성에 해당.
# 클래스 속성: self.속성 에 할당하는 것이 아니라 class 안에서 바로 할당.

'''
객체 생성시 인수로 값을 받는 것이 아닌, 기본적으로 공통된 값을 가지는 속성을 정의하고 할 때 사용.

이런 경우 타 언어에서는 const, final 등의 키워드로 상수로 지정하는 경우가 많은데, Python 에는 상수가 존재하지 않음.
관례적으로 대문자로만 선언된 클래스 속성을 상수로 취급한다고는 하지만, 변경이 불가능한 게 아니므로 주의가 필요.
'''

# 상수 테스트
print("\n# 상수 테스트")


class HaveConst:
    CONST_VALUE = '상수?'
    UN_VARIABLE = '상수???'

    def __init__(self):
        pass


const = HaveConst()
print(const.CONST_VALUE)

const.CONST_VALUE = '변경되지롱.'
print(const.CONST_VALUE)

# 객체 생성시 인수로 받지는 않지만, 기본적으로 공통된 값을 속성으로 지정할 때 사용.
# 그러나, 값을 변경 불가능하도록 지정할 수 없으므로, 이런 암묵적인 관례를 지키는 게 중요.


# 심지어 정의되지 않은 속성 추가 가능.
print("\n# 심지어 정의되지 않은 속성 추가 가능.")

b = MyClass()

print(b.attr)

b.text = 3

print(b.text)
print(type(b))

# 클래스에 정의되지 않은 속성을 객체에 추가적으로 부여할 수 있음.

'''

이러한 점은 클래스에 정의된 속성을 가지지 않으면 에러가 발생하는 Java 나 C계열 언어 등의 컴파일러 언어와 달리
클래스에 제약이 적고 상당히 자유로워, '틀' 이라는 역할을 제대로 수행할 수 있을지 의문이 들지만,

NoSql, 빅데이터 등의 비정형 데이터를 다루는데는 유리한 측면도 있을 것으로 예상됨. 

'''

# b = MyClass('test')  하지만, 객체 생성시에는 이런 식으로 생성자에 정의되지 않은 속성을 넣을 수 없음.

# Traceback (most recent call last):
#   File "<stdin>", line 1, in < module >
# TypeError: MyClass() takes no arguments


# 1.4 메소드
print("\n[ 1.4 메소드] ─────────────────────────────────────────────────────────────────────────────────────────────\n")

a = Human('고길동', 40, '남성')

a.showSelf()

# Python 오버라이딩 불가
print("\n# Python 오버라이딩 불가")

ss = Car("씽씽이", 2021, 'Blue', 1000000)

# ss.discount()
# TypeError: discount() missing 1 required positional argument: 'percentage'

ss.discount(.1)
