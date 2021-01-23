# 파이썬 기초 (+카카오톡 챗봇) 스터디 2주차

# python 클래스
# 2. 상속

# 2.1 생성 및 호출
print("\n[ 2.1 생성 및 호출 ] ──────────────────────────────────────────────────────────────────────────────────────\n")

from classes import *


a = Bird("부엉이")
print(a.name, a.__class__)

a.fly()

# 부모 클래스의 메소드 호출
print("\n# 부모 클래스의 메소드 호출")

b = Pigeon('비둘기')
print(b.name, b.__class__)

b.fly()

print(b.leg)

# Pigeon 클래스에는 아무것도 정의도지 않았음에도, Bird 클래스의 메소드 사용 가능.


# 2.2 오버라이딩
print("\n[ 2.2 오버라이딩 ] ────────────────────────────────────────────────────────────────────────────────────────\n")

c = Chicken('닭')
print(c.name, c.__class__)

c.fly()

d = Bird("종달새")

d.fly()

# Bird 클래스의 fly() 메소드는 기존과 동일함.

# super() 메소드
print("\n# super() 메소드")

e = Eagle('독수리')
print(e.name, e.__class__)

e.fly()


# 2.3 다중 상속
print("\n[ 2.3 다중 상속 ] ─────────────────────────────────────────────────────────────────────────────────────────\n")

man = Man()

man.work()
man.playWithKids()
man.speak()

# mro() 메소드
print("\nmro() 메소드")

print(Man.mro())
