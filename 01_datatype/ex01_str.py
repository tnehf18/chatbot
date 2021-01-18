# 파이썬 기초 (+카카오톡 챗봇) 스터디 1주차

# python 자료형
# 1. 문자열 str

# 1.1 생성 방법
print("\n[ 1.1 생성 방법 ] ─────────────────────────────────────────────────────────────────────────────────────────\n")

msg1 = '파이썬 자료형을 학습중입니다.'
msg2 = "파이썬 자료형을 학습중입니다."

print(msg1, type(msg1))
print(msg2, type(msg2))

# * 위 두 결과는 동일하므로, javaScript 처럼 작은 따옴표와 큰 따옴표를 활용 가능.
#    ex) "It's a fine day.", 'He said loudly, "The end will comes".'

# - 멀티라인 문자열 표현(줄바꿈 포함문자열)
# - '''문자열(줄바꿈 포함)''' ("""문자열(줄바꿈 포함)""" ※ 동일함.)

msg3 = '''아무개님께,

이 편지는 영국에서 최초로 시작되어 일년에 한 바퀴 돌면서 받는 사람에게 행운을 주었고
지금은 당신에게로 옮겨진 이 편지는 4일 안에...'''

msg4 = "아무개님께,\n\n이 편지는 영국에서 최초로 시작되어 일년에 한 바퀴 돌면서 받는 사람에게 행운을 주었고\n지금은 당신에게로 옮겨진 이 편지는 4일 안에..."

print(msg3, type(msg3))

print(msg4, type(msg4), msg3 == msg4)

# Tip. DB 쿼리문 작성시 용이하다고 함.
query = '''
select *
  from emp
 where deptno = {no}
 order by eno desc
'''

print(query)


# 1.2 문자열 연산
print("\n[ 1.2 문자열 연산 ] ───────────────────────────────────────────────────────────────────────────────────────\n")

text1 = "반갑습니다. "
text2 = "나는 홍길동입니다."

# + 더하기
print(text1 + text2)

# * 곱하기 (반복)
print(text2 * 2)

# in 키워드
text3 = "나는 자유다!"
print("자유" in text3)

print("자유" not in text3)


# 1.3 문자열 포맷
print("\n[ 1.3 문자열 포맷 ] ───────────────────────────────────────────────────────────────────────────────────────\n")

# 문자열 포맷 코드 활용
fmt1 = "I eat %d apples."
print(fmt1 % 3)

fmt2 = "I eat %s apples." % "five"
print(fmt2)

number = 10
fruit = "사과"
print("나는 과일가게에서 %s %d개 샀다." % (fruit, number))


# format() 함수 활용
age = 20
txt = "나는 {}살 입니다."
print(txt.format(age))

number = 2
food = "라면"
area = "식당"
txt = "나는 {}에서 {}을 {}개 먹었다."
print(txt.format(area, food, number))

number = 2
food = "라면"
area = "식당"
txt = "나는 {2}에서 {1}을 {0}개 먹었다."
print(txt.format(number, food, area))

txt = "나는 {area}에서 {food}을 {number}개 먹었다."
print(txt.format(area="식당", food="라면", number=2))


# f 키워드 활용시, list 나 dict도 활용가능. (파이썬 3.6 이상에서만 가능.)
name = '홍길동'
age = 30
print(f'나의 이름은 {name}입니다. 나이는 {age}입니다.')

list1 = ['홍길동', 30]
print(f'나의 이름은 {list1[0]}입니다. 나이는 {list1[1]}입니다.')

dict1 = {'name':'홍길동', 'age':30}
print(f'나의 이름은 {dict1["name"]}입니다. 나이는 {dict1["age"]}입니다.')

# 알림용 문장 출력시 유용할 것으로 생각됨.


# 1.4 문자열 관련 함수
print("\n[ 1.4 문자열 관련 함수 ] ──────────────────────────────────────────────────────────────────────────────────\n")

"""

* count()           : 문자열에 특정 단어가 몇 개 포함되어 있는지 return.
* format()          : 문자열에 지정된 위치에 지정된 형식의 값을 삽입함.
* find() / index()  : 문자열에 특정 단어가 시작하는 위치를 return.
* replace()         : 문자열에서 특정 단어를 다른 단어로 치환. (* 전부 치환, default, option으로 치환 횟수 지정 가능. )
* split()           : 문자열을 특정 단어 기준으로 쪼개어 list로 return.
* join()            : 문자열을 인자의 사이사이에 반복하여 집어넣어 하나의 문자열로 만듦.
* lower() / upper() / capitalize() / swapcase() : 대소문자 변환.
* strip()  / lstrip() / rstrip()  : 공백 제거.
* startswith() / endswith() : 문자열이 특정 단어로 시작 또는 끝나는지 여부를 return.
* encode()          : 문자열을 ASCII 코드 등으로 인코딩 함.
* isalnum() / isalpha() / isdecimal() / isnumeric() 등 : 문자열의 표현 형태를 확인.
* zfill()           : 특정 길이 만큼 문자열의 앞을 "0" 으로 채움.

"""

# count()
print("\n# count()")
txt = "I love apples, apple are my favorite fruit"

print(txt.count("apple"))

# format()
print("\n# format()")

txt = "For only {price:.2f} dollars!"

print(txt.format(price = 49))

# {} 안에는 placeholder 라는 문자열 포맷 표현식이 존재함. 레퍼런스를 참조할 것.

# find()
print("\n# find() / index()")

txt = "Hello, welcome to my world."

print(txt.find("welcome"))
print(txt.index("welcome"))

# find()와 index()는 거의 동일하지만, 값을 찾지 못할 경우, index()는 -1을 return 하는 반면, index 는 에러가 발생함에 주의.
# 그런 주제에 list 에는 index() 함수만 존재한다는 점이 참 난감함...

# replace()
print("\n# replace()")

txt = "정 과장과 김 과장은 출장이 예정되어 있고, 이 과장은 내근입니다."

print(txt.replace("과장", "차장"))
print(txt.replace("과장", "차장", 2)) # 횟수 지정 가능.

# split()
print("\n# split()")

print("가 나 다 라 마".split())  # 기본값으로 공백이나 탭 등을 기준으로 쪼개어 줌.
print("가    나   다   라   마".split())  # 기본값으로 공백이나 탭 등을 기준으로 쪼개어 줌.

print("가 나 다 라 마".split()[0])  # 이렇게 바로 꺼낼 수 있으며, 실제로 많이 사용함.

print("가,나,다,라,마".split(","))

print("가,나,다,라,마".split(",", 2))  # 횟수 지정 가능.

# join()
print("\n# join()")

print(",".join("가나다라마"))  # 문자열의 경우, 문자 사이사이에 문자를 삽입하여 return.

list1 = ["가", "나", "다", "라", "마"]
print(",".join(list1))  # 일반적으로 list, tuple 등의 자료구조 형태의 자료형을 문자열 하나로 나타낼 때 많이 활용.

dict1 = {"name": "Ford", "model": "Mustang"}
print(",".join(dict1))  # 그러나, dict 의 경우에는 key 만 꺼내서 문자열로 묶을 뿐, value 를 가져오지는 않음.


# lower() / upper() / capitalize() / swapcase()
print("\n# lower() / upper() / capitalize() / swapcase()")

txt = "I'm your %I father."

print(txt.upper())
print(txt.lower())
print(txt.casefold())
# lower() 함수와 완전히 동일해보이고, 옵션도 없으나, casefold() 는 유니코드 문자도 소문자로 치환한다고함. 그러나, 겨우 소문자 치환에 거기까지 쓸 일은 없을 듯.

print(txt.lower().capitalize())
print(txt.swapcase())


# strip()  / lstrip() / rstrip()
print("\n# strip()  / lstrip() / rstrip()")

txt = "    대한민국 서울     "

print(txt.strip())   # print : '대한민국 서울'
print(txt.rstrip())  # print : '    대한민국 서울'
print(txt.lstrip())  # print : '대한민국 서울     '


# startswith() / endswith()
print("\n# startswith() / endswith()")

txt = "가나다라마바사아자차카타하"

print(txt.startswith("가"))
print(txt.endswith("타"))

# 내부적으로는 byte 로 동작하는지, 한글의 경우, start와 end 위치 지정시 문제가 있다.
print(txt.startswith("가", 0))  # True
print(txt.startswith("나", 1))  # False
print(txt.startswith("나", 2))  # True
print(txt.startswith("다", 4))  # True

# 인자로는 prefix 의 구분자 하나만 넣을 것을 권장함.


# zfill()
print("\n# zfill()")

txt = "가나다라마바사아자차카타하"

print(txt.zfill(20))
