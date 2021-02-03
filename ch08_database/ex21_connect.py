# 파이썬 기초 (+카카오톡 챗봇) 스터디 3주차

# python 데이터베이스
# 1. 데이터베이스

"""
MySQL 8.0 으로 진행함.
"""

# 1.1 설치 및 연결
print("\n[ 1.1 설치 및 연결 ] ──────────────────────────────────────────────────────────────────────────────────────\n")

print('''
* 많이 사용하는 Python 의 MySQL 연동 라이브러리
  - mysql-connection-python
  - PyMySQL
  - pyhive
  - prestodb
  - MySQLdb
    
  ※ 약간의 차이는 있으나, 대부분 비슷하게 동작하므로 본인에게 편한 걸 권장.
  
  > 본 챕터에서는 교재에서 소개하는 MySQL 5.5 와 MariaDB 5.5 이상을 지원하는 PyMySQL 모듈을 설치하여 진행.
  
  
  # 모듈 설치
  
  > pip install pymysql
  
  설치 완료시 파이썬 접속 후, import pymysql 실행하여 정상 유무 확인.  # 이상 없을시 정상 설치 완료.
  
  host      : 127.0.0.1 (localhost)
  user      : chatbot
  password  : 0000
  schema    : chatbot
  charset   : utf8mb4
''')


if input("위와 같이 MySQL 설치 및 사용자 권한 부여까지 완료 하셨습니까? (y/n): ").lower() != 'y':
    print("MySQL 설치 및 사용자 권한 부여 후 진행하시길 바랍니다.")
    quit()


import datetime as dt
import pymysql

db = pymysql.connect(
    host='localhost',       # 호스트명
    user='chatbot',         # 사용자 계정
    password='0000',        # 사용자 비밀번호
    db='chatbot',           # 스키마
    charset='utf8'          # 인코딩
)

print(db, type(db))

print(dir(db))

print(db.host)
print(db.host_info)
print(db.user)
print(db.password)
print(db.db)
print(db.charset)

db.close()  # 작업 수행 후에는 반드시 DB Connection 을 해제할 것.

# 단 위의 경우 보다 아래처럼 try 문 활용을 권장.

db = None
try:
    db = pymysql.connect(
        host='127.0.0.1',
        user='chatbot',
        password='0000',
        db='chatbot',
        charset='utf8'
    )

    '''
    쿼리 등 DB 작업
    '''

except Exception as e:
    print(f"[DB 연결 실패]: [{dt.datetime.now()}] {e}")
else:
    print(f"[DB 연결 성공]: {db.host_info} {db.user.decode('utf-8')} [{dt.datetime.now()}]")

    '''
    메시지 등, 쿼리 수행 완료시 수행할 코드
    '''

finally:
    if db is not None:
        db.close()
        print(f"[DB 접속 해제]: {db.host_info} {db.user.decode('utf-8')} [{dt.datetime.now()}]")


# 1.2 테이블 생성
print("\n[ 1.2 테이블 생성 ] ───────────────────────────────────────────────────────────────────────────────────────\n")

db = None
try:
    db = pymysql.connect(
        host='127.0.0.1',
        user='chatbot',
        password='0000',
        db='chatbot',
        charset='utf8'
    )

    sql = '''
    CREATE TABLE tb_student (
        id      INT     PRIMARY KEY AUTO_INCREMENT NOT NULL,
        name    NVARCHAR(30),
        age     INT,
        address NVARCHAR(100)

    ) ENGINE = innoDB DEFAULT CHARSET=utf8
    '''

    # cursor: DB 작업을 수행해주는 객체
    cursor = db.cursor()

    # execute(): 쿼리 실행 함수
    cursor.execute(sql)

except Exception as e:
    print(f"[DB 연결 실패]: [{dt.datetime.now()}] {e}")
else:
    print(f"[DB 수행 성공]: {db.host_info} {db.user.decode('utf-8')} [{dt.datetime.now()}]", sql)
finally:
    if db is not None:
        db.close()
        print(f"[DB 접속 종료]: {db.host_info} {db.user.decode('utf-8')} [{dt.datetime.now()}]")


# db 객체 값 및 연결 상태 확인
print(db, db.open if db is not None else None, db.db)


# 스키마 생성 및 변경
print("\n# 스키마 생성 및 변경")

'''
※ 사실 pymysql 의 connect() 함수에 db, 즉, 스키마는 필수가 아니고, 사용자에게 스키마에 권한만 있다면
  데이터베이스를 Python 에서 바로 생성하거나 접속한 현재 스키마를 변경할 수도 있음.
  
  그러나, 역시나 db 사용자 계정에 대한 권한 문제 때문에, (특히나 MySQL 은 더) 
  
  일반적으로 Python 에서 직접 스키마나 사용자 계정을 생성하거나 다루는 것은 권장되는 사항은 아님.
  
  따라서 아래의 예제는 참조만 하고, 실행할 경우 생성된 스키마는 DROP 으로 삭제를 권장함. 
'''


db = None
try:
    db = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password=input("root 계정 비밀번호를 입력해주세요: ")     # 본인의 root 계정의 비밀번호를 입력해주세요.
    )

    sql = '''
    CREATE DATABASE temp CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
    '''

    # cursor: DB 작업을 수행해주는 객체
    cursor = db.cursor()

    # execute(): 쿼리 실행 함수
    cursor.execute(sql)

    # db 스키마 변경 함수
    db.db = "temp"
    db.select_db(db.db)     # select_db 로만 스키마 변경이 가능하며, select_db 함수는 return 이 없어서 객체의 db 속성값이 갱신되지 않으므로 이렇게 할 것을 권장.

    sql = '''
    CREATE TABLE tb_student (
        id      INT     PRIMARY KEY AUTO_INCREMENT NOT NULL,
        name    NVARCHAR(30),
        age     INT,
        address NVARCHAR(100)

    ) ENGINE = innoDB DEFAULT CHARSET=utf8
    '''

    cursor = db.cursor()
    cursor.execute(sql)

except Exception as e:
    print(f"[DB 연결 실패]: [{dt.datetime.now()}] {e}")
else:
    print(f"[DB 수행 성공]: {db.host_info} {db.user.decode('utf-8')} [{dt.datetime.now()}]", sql)
finally:
    if db is not None:
        db.close()
        print(f"[DB 접속 종료]: {db.host_info} {db.user.decode('utf-8')} [{dt.datetime.now()}]")


# 생성된 temp 스키마는 단순히 예제 확인을 위한 용도이므로 이후 삭제를 권장합니다.
