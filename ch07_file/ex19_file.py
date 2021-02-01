# 파이썬 기초 (+카카오톡 챗봇) 스터디 3주차

# python 파일처리
# 1. 파일

# 1.1 기본 형태
print("\n[ 1.1 기본 형태 ] ─────────────────────────────────────────────────────────────────────────────────────────\n")

print('''
  변수명 = open("파일명", "옵션")
  
  ...
  
  변수명.close()
  
  
  r : 읽기 전용 - (기본값) 파일의 내용을 읽어들일 순 있지만 내용을 변경할 수 없음. 파일을 못 찾으면 에러.
  a : 이어 쓰기 - 파일의 끝에 내용을 덧붙임. (원본 내용 변경 불가), 파일을 못 찾으면 새 파일 생성.
  w : 덮어 쓰기 - 파일의 내용을 작성. 기존 파일이 없을 경우 새 파일 생성하여 작성. 이미 파일이 존재하는 경우, 기존에 있던 내용을 덮어씀.
  x : 새로 쓰기 - 파일의 내용을 작성. 새 파일 생성하여 작성. 파일이 이미 존재하는 경우 에러.
  
  t : 텍스트 - (기본값) 텍스트 편집.
  b : 바이너리 - 바이너리 형식 파일 편집.
''')


file = open("sub_dir/textfile.txt")
print(file)

file.close()


# with 키워드
print("\n# with 키워드")

with open("sub_dir/textfile.txt", "r") as file:
    print(file)


# 파일이 닫혔는지 확인 여부 closed 속성 -> bool

print(file.closed)


# 1.2 읽기
print("\n[ 1.2 읽기 ] ──────────────────────────────────────────────────────────────────────────────────────────────\n")

# read()
print("# read()")

'''
f = open("textfile.txt", "r")

content = f.read()
print(content)

f.close()
'''

# UnicodeDecodeError: 'cp949' codec can't decode byte 0xec in position 6: illegal multibyte sequence
# 텍스트 파일은 인코딩이 cp949 인데, 현재 IDE의 기본 인코딩이 utf-8 이라서 인코딩 에러가 발생.

# 따라서 아래와 같이 변경 해줘야 함.

f = open("sub_dir/textfile.txt", "r", encoding="utf-8")

content = f.read()
print(content)

f.close()


# f = open("textfile.txt", "r")
# f.encoding = "utf-8"

# 이렇게 시도해 보았지만, 변경 불가능한 속성이라면서 에러가 발생했다.
# AttributeError: readonly attribute


# read() 에 인수로 정수로 입력하면 글자수만큼 읽어들임.

f = open("sub_dir/textfile.txt", "r", encoding="utf-8")

content = f.read(5)
print(content)


# readline() / readlines()
print("\n# readline() / readlines()")

with open("sub_dir/management.csv", "r") as file:
    print(file)


# readline(): 한줄 씩 읽어들이는 예제

with open("sub_dir/management.csv", "r") as file:
    result = []

    line = file.readline()

    while len(line) > 0:
        result.append(line.strip("\n").split(","))
        line = file.readline()
    else:
        print(result)


# readlines(): 각 줄을 읽어들여 리스트로 반환


with open("sub_dir/management.csv", "r") as file:
    result = []

    lines = file.readlines()

    for line in lines:
        result.append(line.strip("\n").split(","))
    else:
        print(result)

'''
# 축약표현

with open("management.csv", "r") as file:

    lines = file.readlines()

    print(line.strip("\n").split(",") for line in lines)
'''


# 1.3 생성 및 쓰기
print("\n[ 1.3. 생성 및 쓰기 ] ─────────────────────────────────────────────────────────────────────────────────────\n")

# write()
print("\n# write()")


file = open("newfile.txt", "w")

content = '''
계절이 지나가는 하늘에는
가을로 가득 차 있습니다.
'''

file.write(content)
file.close()

file = open("newfile.txt", "r")

content = file.read()
print(content)

file.close()


# 이어 쓰기도 함수는 동일하게 write() 함수를 사용함.
print("\n# 이어 쓰기")

file = open("newfile.txt", "a")

content = '''
나는 아무 걱정도 없이
가을 속의 별들을 다 헬 듯합니다.
'''

file.write(content)
file.close()

file = open("newfile.txt", "r")

content = file.read()
print(content)

file.close()


# 1.4 파일 제거
print("\n[ 1.4. 파일 제거 ] ────────────────────────────────────────────────────────────────────────────────────────\n")

# os 모듈이 필요.

import os

yon = input("생성된 newfile.txt 파일을 제거하시겠습니까? (Y/N) \n")
if yon == "Y":
    os.remove("newfile.txt")
    print("newfile.txt 파일이 제거되었습니다.")
elif yon == "N":
    pass
else:
    print("Y 혹은 N 로만 입력해주세요.")

