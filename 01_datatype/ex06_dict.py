# 파이썬 기초 (+카카오톡 챗봇) 스터디 1주차

# python 자료형
# 6. 딕셔너리 dict

# 순서를 갖지 않음. (출력시 랜덤한 순서로 나타남.)
# key 는 중복을 허용하지 않음.

# 자료형의 중복을 제거하기 위한 필터 역할로 종종 사용하기도 한다.

# 6.1 생성 방법
print("\n[ 6.1 생성 방법 ] ─────────────────────────────────────────────────────────────────────────────────────────\n")

# 중괄호 { }를 사용하며, 요소는 key 와 value 를 콜론(:)으로 한 쌍으로 묶어서 표현.

car = {
    "name": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(car)

# 요소 추가/수정

car['price'] = 10000
print(car)

car['price'] = 20000
print(car)

# 요소 삭제

del car["year"]
print(car)


# 주의사항: 딕셔너리에서 key 는 고유한 값이므로 중복불가

a = {1: 'a', 1: 'b'}
print(a)
{1: 'b'}

# key 에 리스트(변경 가능)는 쓸 수 없음.튜플(변경 불가능)은 사용 가능.

a = {
    (1, 2, 3): True,
    'B': [1, 2, 3]
}
print(a[(1, 2, 3)])


# 6.2 dict 관련 함수
print("\n[ 6.2 dict 관련 함수 ] ────────────────────────────────────────────────────────────────────────────────────\n")

"""

* clear()	    : 딕셔너리 안의 요소를 모두 제거.
* copy()	    : 딕셔너리를 복사하여 제공. (*깊은 복사)
* fromkeys()	: 키와 값으로 묶어 딕셔너리로 return.
* get()	        : 딕셔너리에서 해당하는 키로 값을 return.
* keys()	    : 키들을 list 로 return.
* values()	    : 값들을 list 로 return.
* items()	    : 키와 값을 한 쌍으로 tuple 로 묶어, list 로 return. (* 단순히, value 만 return 되는 것이 아님에 주의.)
* pop()	        : 딕셔너리에서 키에 해당하는 값을 꺼내면서 삭제. (인자로 키 필수.)
* popitem()	    : 마지막에 입력된 key 요소를 제거.
* setdefault()	: 딕셔너리에 해당 key 와 value 를 추가하고 value 값을 return. 단, 이미 key가 있는 경우, 기존 키의 값을 return만 함.
* update()	    : 딕셔너리에 해당 key 와 value 를 추가하거나 해당 키의 값을 바꿈. (* 인자로 dict 형태로 넣어야 함.)

"""

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print("car", car)

# fromkeys()
print("\n# fromkeys()")

keys = ('key1', 'key2', 'key3')
value = 'value'

dict1 = dict.fromkeys(keys, value)

print(dict1)

# 그러나 value 에 list 와 같은 자료구조형을 입력해도, 알아서 key 와 value 를 자동으로 맞춰주는 것이 아니므로 활용성은 낮음.

keys = ('key1', 'key2', 'key3')
values = (1, 2, 3)

dict2 = dict.fromkeys(keys, values)

print(dict2)


# get()
print("\n# get()")

print(car.get("model"))

# 단, dict[키 이름] 의 경우, key 가 존재하지 않을 경우 에러가 발생하지만,
# get 함수를 쓸 경우, key 가 존재하지 않으면 None 으로 return 한다.

print(car.get('price'))

# print(car['price'])
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'car' is not defined


# keys()
print("\n# keys()")

keys = car.keys()
print(keys, type(keys))

# values()
print("\n# values()")

values = car.values()
print(values, type(values))

# keys(), values() 의 return 결과는 list 의 하위 class 인 것으로 보임.
# 타입이 list 가 아니라서, list 의 내장 함수들을 바로 사용할 수 없으며, 직접적으로 요소값을 변경하는 것은 가능.

# values[0] = 'Benz'
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'dict_values' object does not support item assignment


# items()
print("\n# items()")

items = car.items()
print(items, type(items))

# 독특하게, key 와 value 를 한 쌍으로 묶어 tuple 로 이루어진 list 를 return.
# 때문에, dict 의 반복문 사용법이 특이하고, tuple 자체는 그다지 활용성이 적어도 숙지의 중요성이 큼.

x = car.items()

car["year"] = 2018

print(x, type(x))

# keys(), values(), items() 모두 반환되는 결과는 변경이 불가능하지만, 메모리를 참조하는 것처럼 동작하므로
# dict 가 변경되더라도 그 변경사항이 반영됨.


# pop()
print("\n# pop()")

print(car.pop('year'))
print(car)

# get() 은 값을 가져와도, dict 가 그대로지만, pop() 은 값을 가져오면서, 해당 키가 제거된다.


# popitem()
print("\n# popitem()")

print(car.popitem())


# setdefault()
print("\n# setdefault()")

print(car.setdefault('year', 2021))

car['year'] = '1964'

print(car.setdefault('year', 2021))


# update()
print("\n# update()")

car.update({"color": "White"})

print(car)
