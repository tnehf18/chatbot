# 파이썬 기초 (+카카오톡 챗봇) 스터디 3주차

# python 모듈
# 2. 기본 라이브러리

# 2.1 라이브러리 종류
print("\n[ 2.1 라이브러리 종류 ] ───────────────────────────────────────────────────────────────────────────────────\n")

print('''
* 시스템 관련     : sys, os, platform
* 날짜, 시간 관련 : datetime, time, calendar
* 수학 관련       : math, decimal, random, statistics
* 텍스트 처리     : re
* 파일 관련       : pickle, fileinput, shutil, glob, tempfile
* 입·출력 관련    : io
* 병렬 처리       : threading
* 네트워킹        : socket, http, webbrowser, json
''')

# 그러나, 사실 기본 라이브러리를 그대로 쓰는 사람은 많지 않다.
# CS나 웹 개발 등의 비즈니스 로직을 개발하는 개발자들은 다른 사람이 만들어진 좀 더 편리한 라이브러리를 사용하고,
# 이런 개발자들을 위한 라이브러리들을 만드는 이들이 주로 기본 라이브러리를 응용하고자 사용하는 편.

# 2.2 시스템 관련
print("\n[ 2.2 시스템 관련 ] ───────────────────────────────────────────────────────────────────────────────────────\n")

# sys 파이썬 시스템 관련
print("\n# sys 파이썬 시스템 관련")

import sys

print(sys.argv)
for i in range(len(sys.argv)):
    print(f"{i}번째 인수: {sys.argv[i]}")


# sys.exit()  # 파이썬 모듈을 종료하고 빠져나감. 인터프리터 상에서 exit() 를 입력하여 나가는 것과 동일함.

print("꺄아아아아아악")


# os 운영 체제 관련
print("\n# os 운영 체제 관련")

import os

print(os.environ)

print(os.environ['PYTHONPATH'])


# 2.3 시간, 날짜 관련
print("\n[ 2.3 시간, 날짜 관련 ] ───────────────────────────────────────────────────────────────────────────────────\n")


# time 시간 관련
print("\n# time 시간 관련")

import time as t, datetime as dt, calendar as cld

print(t.time())
# 1970년 1월 1일 0시 0분 0초 기준으로 현재까지의 경과 시간을 초로 나타냄.

cur_time = t.localtime()
print(cur_time, type(cur_time))
print(cur_time[0])

print(t.strftime("현재 시각: %Y-%m-%d %H:%M:%S", cur_time))


# time 모듈의 sleep(): 지연 가능.

for i in range(1, 6):
    print(i)
    t.sleep(.5)
else:
    print("땡~")


# datetime 날짜 관련
print("\n# datetime 날짜 관련")

now = dt.datetime.now()

print(now)
print(now.year)
print(now.strftime("%c"))

x = dt.datetime(2021, 1, 29)

print(x)


# calendar 날짜 관련
print("\n# calendar 날짜 관련")

print(cld.calendar(2021))
print(cld.weekday(2021, 1, 29))  # 해당 날짜의 요일을 0 ~ 6 까지 숫자로 return
print(cld.monthrange(2021, 2))


# 날짜 시간 관련된 모듈은 내장, 외장 모듈을 포함해 본인에게 편한 것을 이용하면 됨.


# 2.4 숫자 관련
print("\n[ 2.4 숫자 관련 ] ─────────────────────────────────────────────────────────────────────────────────────────\n")


# random 난수 생성
print("\n# random 난수 생성")

import random as r

print(r.random())  # 0 ~ 1 사이의 실수
print(r.randint(1, 100))  # 1 ~ 100 사이의 정수

numbers = [1, 2, 3, 4, 5]
r.shuffle(numbers)  # 순서가 있는 자료형의 순서를 임의적으로 섞음.

print(numbers)

# math 수학 관련
print("\n# math 수학 관련")

import math

print(math.pi)
print(math.e)

print(math.ceil(12.265))  # 올림
print(math.floor(12.265))  # 버림


# 삼각함수도 제공하지만 오차가 너무 커서 안 쓰는 게 나음.


# 2.5 정규 표현식
print("\n[ 2.5 정규 표현식 ] ───────────────────────────────────────────────────────────────────────────────────────\n")


# re 정규 표현식
print("\n# re 정규 표현식")

import re

text = """
park 800905-1049118
kim  700905-1059119
"""

regex = re.compile("(\d{6})[-]\d{7}")
print(regex.sub("\g<1>-*******", text))


# match()
print("\n# match()")

regex = re.compile('[a-z]+')

print(regex.match("python"))
print(regex.match("3 python"))


# search()
print("\n# search()")

print(regex.search("python"))
print(regex.search("3 python"))

# findall()
print("\n# findall()")

print(regex.findall("life is egg"))


# 개인적으로 Python 의 정규식은 모듈을 타 언어보다 번거로워 보임.
