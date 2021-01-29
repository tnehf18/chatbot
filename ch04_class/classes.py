# classes.py

# 빈 클래스
class Empty:
    pass


class Human:

    # 기본 생성자
    # def __init__(self):
    #     pass

    # ※ Python 에서는 생성자를 오버로딩으로 여러개 정의하는 것 자체는 가능하지만,
    # 외부에서 마지막에 정의 함수만 인식하므로 생성자는 하나만 정의해야 함.

    def __init__(self, name, age, gender):
        self.name = name,
        self.age = age,
        self.gender = gender

    def showSelf(self):
        print("안녕하세요. 나는 %s입니다." % self.name)


# 생성자의 다형성 구현 방법. (유사 오버로딩)
class Person:

    def __init__(self, name=None, age=None, gender=None):
        self.name = name
        self.age = age
        self.gender = gender


# 하지만, 이렇게 하면 변수가 None 이라는 값을 가지고 모두 생성되어 버리기 때문에, Python 에서 권장하는 방법은 아님.


class Student:

    def __init__(self, name=None, age=None, gender=None, str_to_std=None):
        if str_to_std:
            attr_list = str_to_std.split(',')
            self.name = attr_list[0]
            self.age = int(attr_list[1])
            self.gender = str(attr_list[2])
        else:
            self.name = name
            self.age = age
            self.gender = gender


# 또한, 다양한 방법으로 객체를 생성하고자 __init__ 함수에 매개변수를 추가할수록,
# 생성된 객체 안에 None 값을 가진 불필요한 속성이 늘어나게 됨.
# 그리고 모든 다른 경우에 대해 if 문으로 분기처리를 해주어야 한다.


# 언더스코어(_) 활용법 1.
class Cat:
    _internal_kind = '고양이'
    _internal_bone = '액체'

    def __init__(self, name):
        self.name = name

    def sentence(self):
        return "%s %s는 %s입니다(?)" % (self._internal_kind, self.name, self._internal_bone)


# 언더스코어(_) 활용법 2.
class A:
    attr1 = '속성A'
    __attr2__ = '고유 속성A'


class B(A):
    __attr2__ = '고유 속성B'


# 서로 같은 이름의 속성을 가지지만 오버라이드가 되지 않는다.


# 클래스 속성과 인스턴스 속성
class Flight:
    class_attr = []

    def __init__(self):
        self.class_attr = []

    def add_instance_attr(self, number):
        self.class_attr.append(number)

    def add_class_attr(self, number):
        Flight.class_attr.append(number)


class Car:

    def __init__(self, name, year, color, price):
        self.name = name
        self.year = year
        self.color = color
        self.price = price

    def discount(self):
        print("지금 %s가 할인중입니다. 할인율: 10%" % self.name)

    def discount(self, percentage):
        print("지금 %s가 할인중입니다. 할인가: %d" % (self.name, self.price * (1 - percentage)))


# 상속
class Bird:

    def __init__(self, name, wing=2, leg=2):
        self.name = name
        self.wing = wing
        self.leg = leg

    def fly(self):
        print("%s가 하늘을 납니다." % self.name)


class Pigeon(Bird):
    pass


class Chicken(Bird):

    def fly(self):
        print("슬프지만 닭은 하늘을 날 수 없습니다.")


class Eagle(Bird):

    def fly(self):
        super().fly()
        print("굉장히 멋있게 납니다.")

    # 단, 부모 클래스의 속성을 가져올 때는, 인스턴스 속성을 가져올 수 없음. -> 클래스 속성이 필요함.

    # def fly(self):
    #     print("%d개의 날개를 펼칩니다." % super().wing)
    #     super().fly()

    # AttributeError: 'super' object has no attribute 'wing'


# 다중 상속
class Father:
    def playWithKids(self):
        print('자식들과 즐겁게 놉니다.')


class Worker:
    def work(self):
        print('직장에서 일합니다.')


class Man(Father, Worker):
    def speak(self):
        print('쉬고 싶다...')
