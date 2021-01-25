# 파이썬 기초 (+카카오톡 챗봇) 스터디 2주차

# python 함수
# 2. 내장함수

# 2.1 대표적인 내장 함수
print("\n[ 2.1 대표적인 내장 함수 ] ────────────────────────────────────────────────────────────────────────────────\n")

"""

* abs()           :	입력받은 인수를 절대값으로 return.
* round()         :	입력받은 숫자를 반올림하여 return.
* pow()           :	입력받은 인수를 거듭제곱하여 return.

※ ceil(), floor() 등의 올림, 버림은 math 모듈을 import 해야 가능.

* ascii()         :	ascii 코드가 아닌 문자들을 ascii 코드로 변환하여 return.
* chr()           :	유니코드를 인수로 받아, 해당하는 문자를 return.
* ord()           :	특정 문자를 인수로 받아, 해당하는 유니코드를 return.

* bin()           :	입력받은 정수를 이진수로 변환. (* 소수점 포함하는 실수는 불가능.) 
* oct()           :	입력받은 숫자를 8진수로 변환.
* hex()           :	입력받은 숫자를 16진수로 변환.

* bytes()         :	입력받은 인수로 bytes 객체를 생성. (* 인코딩 관련)
* bytearray()     :	입력받은 인수로 bytearray 객체를 생성. 

* input()         :	터미널 등의 콘솔에서 사용자로부터 입력값을 받음.
* print()         :	터미널 등의 콘솔에서 바로 출력하여 나타내주는 함수.
* type()          :	인수로 받은 객체의 타입명을 return.

* format()        :	특정 포맷으로 변경해줌. (* str 객체 안의 format 메소드와는 다름.)

* max()           :	반복가능한 값을 인수로 받아서 그 중 가장 큰 값을 return.
* min()           :	반복가능한 값을 인수로 받아서 그 중 가장 작은 값을 return.
* sum()           :	반복가능한 값을 인수로 받아서 그 요소를 모두 더함.

* range()         :	특정 범위를 return.

* iter()          : 특정 객체를 반복가능한 개체로 만들어 return.
* next()          : 반복가능한 객체로부터 다음 값을 꺼냄.

※ iterator 객체가 기본 list, tuple 객체들보다 구려서 거의 안 쓰임. next() 또한 iterator() 객체에만 사용 가능.

* all()           :	반복가능한 값을 인수로 받아, 인수의 모든 요소가 참이면 True, 하나라도 False 이면 False 를 return.
* any()           : 반복가능한 값을 인수로 받아, 인수 중 하나라도 참이면 True, 아니면 False. 

* slice()         :	순서가 있는 자료형을 인수로 받아, 특정 위치의 값을 꺼내거나 특정 구간을 잘라서 return 함.
* reversed()      :	순서가 있는 자료형을 거꾸로 정렬하여 return.
* sorted()        :	순서가 있는 자료형을 정렬하여 return.

* enumerate()     :	순서가 있는 자료형(리스트, 튜플, 문자열)을 인수로 받아 인덱스 값을 포함하는 enumerate 객체를 return.
* filter()        :	반복가능한 값을 인수로 받아서, 모든 요소에 특정 함수를 실행하여 참, 거짓을 판별하여 참인 것들만 return. 
* map()           :	반복가능한 값을 인수로 받아서, 모든 요소에 특정 함수의 결과를 return 으로 받아 list 형태로 return.
* zip()           : 반복가능한 자료형을 인수로 받아서, 각 요소를 묶어 튜플 형태로 return.

* id()            :	해당 객체의 고유한 id 값을 return. (* 메모리 주소는 아님.)
* dir()           :	객체가 가진 속성과 메소드 들을 list 형태로 return.

* getattr()       :	object 의 특정 속성의 값을 가져옴.
* setattr()       :	object 에 특정 속성을 값을 변경.  (* 버전 차이인지는 모르겠으나, 없는 속성을 새로 추가할 수 없음.)
* delattr()       :	object 에 특정 속성 또는 메소드를 제거.
* hasattr()       :	object 에 특정 속성 또는 메소드의 존재 여부를 Ture or False 로 return.

* open()          :	파일을 제어하는 함수. (여기서는 생략)

"""

# abs()
print("\n# abs()")

print(abs(-7.25))

print(abs(3 + 5j))  # 복소수 가능.

# round()
print("\n# round()")

num = 5.76543

print(round(num))
print(round(num, 2))
print(round(num, -1))

# ※ ceil, floor 등의 올림, 버림은 math 모듈을 import 해야 가능.


# pow()
print("\n# pow()")

print(pow(4, 3))  # 4 ** 3 과 동일함.

# ascii() / chr() / ord()
print("\n# ascii() / chr() / ord()")

hg = "이것은 한글입니다."

print(ascii(hg))

print(chr(61))
# print(chr("가"))  # TypeError: an integer is required (got type str)

print(ord("가"))  # 단, 길이가 2개 이상인 문자열은 불가능.

# bin() / ocr() / hex()
print("\n# bin() / ocr() / hex()")

print(bin(8))  # prefix 로 0b 가 붙음.

# print(bin(.625))  # TypeError: 'float' object cannot be interpreted as an integer. 실수는 불가.

print(oct(8))  # prefix 로 0o 가 붙음.

print(hex(11))  # prefix 로 0x 가 붙음.

# bytes() / bytearray()
print("\n# bytes() / bytearray()")

byteStr = bytes(10)  # 0이 10개 들어있는 바이트 객체 생성

print(byteStr, type(byteStr))

'''
# 이게 대체 무슨 외계어인가 싶겠지만, 인코딩 관련 문제 때문에 알아둘 필요가 있음.

문자열을 encode 함수로 인코딩을 하게 될 경우, byte 타입으로 return 되며,
이것을 다시 decode 와 encode 함수를 써줌으로써 다른 인코딩으로 변환이 가능해짐. 
'''

print('안녕'.encode('euc-kr'))
# b'\xbe\xc8\xb3\xe7'

print('안녕'.encode('utf-8'))
# b'\xec\x95\x88\xeb\x85\x95'


text = b'\xbe\xc8\xb3\xe7'.decode('euc-kr')

print(text, text.encode('utf-8'))

'''
엑셀처럼 기본 인코딩이 utf-8 이 아닌 파일로부터 자료를 읽어들여 utf-8 인 프로그램에서 열 경우,
글자가 다 깨지는 현상이 발생하므로 인코딩이 필요한 경우가 존재.

그러나, byte 는 튜플처럼 요소를 변경할 수 없는 타입인 반면, bytearray 는 변경이 가능하여,

byte 보다는 bytearray 로 변환하여 많이 활용. 
'''
print()

byteStr = bytes('안녕', encoding='cp949')
print(byteStr, type(byteStr))

print(byteStr.split())

# byteStr[0] = b'hello'  # TypeError: 'bytes' object does not support item assignment

byteArr = bytearray('안녕', encoding='cp949')
print(byteArr, type(byteArr))

byteArr.append(70)

print(byteArr, byteArr.decode('cp949'))

# input() / print() / type()
print("\n# input() / print() / type()")

print("입력받은 내용은 귀찮으니까 생략합니다.", type(input('아무거나 입력해주시면 계속 실행합니다.\n')))
# input 으로 받은 내용은 기본적으로 모두 str 타입음을 주의.


# format()
print("\n# format()")

# ※ 주의, 기본 내장 함수인 format 과 str 타입의 format 메소드는 동작 방식과 결과가 다르므로 주의.

print(format(0.5, '%'))

print("정수 : {} / 실수 : {} / 문자열 : {}".format(10, 10.0, '"10"'))

# 기본 내장 함수 format() 보다는 문자열의 format 메소드를 더 많이 사용할 듯.


# max() / min() / sum()
print("\n# max() / min() / sum()")

values = [0, 1, 2, 3, 4, 5]

print(max(values))
print(min(values))
print(sum(values))

# range()
print("\n# range()")

range1 = range(5)
range2 = range(0, 5)
range3 = range(0, 10, 2)

print(range1, [num for num in range1], type(range1))
print(range2, [num for num in range2], type(range2))
print(range3, [num for num in range3], type(range3))

# iter()
print("\n# iter()")

fruits = iter(["apple", "banana", "cherry"])

print(next(fruits))
print(next(fruits))
print(next(fruits))


# fruits = ["apple", "banana", "cherry"]
#
# print(next(fruits))  # TypeError: 'list' object is not an iterator
# print(next(fruits))
# print(next(fruits))

# list를 굳이 iter() 객체로 만들어서 쓰는 것보다 그냥 list 그대로 쓰는 게 훨씬 유용해 보임.

# 단, class 정의할 때, __iter__() 와 __next__() 메소드를 재정의하면 좀 쓸만해짐.
# 여기는 클래스 공부하고 오세용.

class MyNumbers:
    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        num = self.num
        self.num += 1
        return num


myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

# all() / any()
print("\n# all() / any()")

a = list(range(0, 5))
print(all(a))

a[0] = -1

print(all(a))

a = list(range(0, 5))
print(any(a))

a.clear()

print(any(a))

# slice()
print("\n# slice()")

strs = ("a", "b", "c", "d", "e", "f", "g", "h")

x = slice(2)
print(strs[x])

x = slice(3, 6)
print(strs[x])

x = slice(0, 8, 3)
print(a[x])

# slice 객체를 만들어서 list 의 순서에 집어넣는 게 굉장히 독특해보임. 근데, 헷갈려서 별로 굳이 안 쓸 듯.


# reversed()
print("\n# reversed()")

alph = ["a", "b", "c", "d"]

ralph = reversed(alph)

for x in ralph:
    print(x)

# sorted()
print("\n# sorted()")

alph = ("h", "b", "a", "c", "f", "d", "e", "g")

print(sorted(alph))
print(sorted(alph, reverse=True))

# reversed 처럼 억지로 객체를 만들어서 집어넣는 것보다는 이게 더 나은 듯.
# 단, tuple 넣었는데 list 로 반환됨. 웬만하면 list 로 반환되는 듯.


# enumerate()
print("\n# enumerate()")

inv = enumerate(['body', 'foo', 'bar'])
print(list(inv))

for idx, value in enumerate(['body', 'foo', 'bar']):
    print(idx, value)

# filter()
print("\n# filter()")


def is_even(number):
    return not number % 2


numbers = range(3, 19)
even_list = list(filter(is_even, numbers))
# filter 함수의 결과는 filter 타입으로 반환되기 때문에, list, tuple, enumerate 등의 다른 객체로 변환 해주어야 함.

print(even_list)


# map()
print("\n# map()")


def myFunc(text):
    return len(text)


lens = map(myFunc, ('apple', 'banana', 'cherry'))

print(tuple(lens))  # map 도 결과가 그대로 map 타입으로 반환되기 때문에, list, tuple, enumerate 등의 다른 객체로 변환 해주어야 함.


# 하나 이상의 반복가능한 자료구조를 대상으로 실행 가능.

def pare(k, v):
    return dict({k: v})


x = map(pare, ('fruit', 'meet', 'meal'), ('apple', 'beef', 'rice'))

print(list(x))


# zip()
print("\n# zip()")

a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")

z = zip(a, b)
print(list(z))

# 길이가 일치하지 않아도, 짧은 쪽에 맞춰서 return.

a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica", "Vicky")

z = zip(a, b)
print(list(z))


a = {"John", "Charles", "Mike"}
b = {"Jenny", "Christy", "Monica"}
c = {3, 2, 1}

z = zip(a, b, c)
print(list(z))


# object() / id() / dir()
print("\n# object() / id() / dir()")

obj = object()

print(type(obj))

print(obj, id(obj))  # 생성된 객체의 메모리 주소와 id 값은 다름.
print(dir(obj))  # a 의 속성과 메소드

# getattr() / setattr() / delattr() / hasattr()
print("\n# getattr() / setattr() / delattr() / hasattr()")


class Obj:

    def __init__(self, attr1=1, attr2=2):
        self.attr1 = attr1
        self.attr2 = attr2


obj = Obj()

setattr(obj, 'attr3', 3)

print(hasattr(obj, "attr3"))
print(getattr(obj, "attr3"))

delattr(obj, "attr3")

'''
del obj.attr3
del obj["attr3"]

등 del 키워드나 다른 방법으로도 속성을 제거 가능.
'''

# print(getattr(obj, "attr3"))  # 없는 속성을 꺼내려고 하면 에러가 발생.
print(hasattr(obj, "attr3"))
