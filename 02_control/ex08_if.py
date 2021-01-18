# 파이썬 기초 (+카카오톡 챗봇) 스터디 1주차

# python 제어문

# 기본적으로 python 의 제어문은 C계열 언어에서 괄호나 중괄호가 쓰이는 것과 달리,
# 띄어쓰기나 탭, 줄바꿈으로 이루어지므로, 이에 유의해야 한다.

# 1. if문

# 기본적으로 if ~ else 의 구조로, 참과 거짓의 조건에 따라 실행하는 형태.

a = int(input("숫자 a를 입력하세요.\n"))
b = int(input("숫자 b를 입력하세요.\n"))

if a > b:
    print("\n" + str(a) + " > " + str(b))
    print("a가 b보다 큽니다.")
else:
    print("b가 a보다 큽니다.")

# elif 문

score = int(input("당신의 국어 성적은 몇 점입니까? "))

if score > 90:
    print("당신의 학점은 A 입니다.")
elif score > 80:
    print("당신의 학점은 B 입니다.")
elif score > 70:
    print("당신의 학점은 C 입니다.")
elif score > 60:
    print("당신의 학점은 D 입니다.")
else:
    print("당신의 학점은 F 입니다.")

# 2. for, while 문

# while 문   : 조건문과 많이 활용.
# for 문     : list, set 등의 자료구조와 많이 활용.
