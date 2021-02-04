# 파이썬 기초 (+카카오톡 챗봇) 스터디 3주차

# python 데이터베이스
# 2. CRUD


import datetime as dt
import pymysql


# DB 연결함수
def conn(host, user, password, schema=None, charset='utf8'):
    __db = None
    try:
        __db = pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=schema,
            charset=charset
        )
    except Exception as e:
        print(f"[DB 연결 실패]: [{dt.datetime.now()}] {e}")
    else:
        print(f"[DB 연결 성공]: {__db.host_info} {__db.user.decode('utf-8')} [{dt.datetime.now()}]")
    finally:
        return __db


# 2.2 데이터 조회
print("\n[ 2.2 데이터 조회 ] ───────────────────────────────────────────────────────────────────────────────────────\n")

db = conn('127.0.0.1', 'chatbot', '0000', 'chatbot', 'utf8')

sql = '''
SELECT * FROM tb_student
'''

cursor = db.cursor()

try:
    cursor.execute(sql)
except Exception as e:
    cursor.rollback()
    print(f"[SQL 에러]: {e.__traceback__}")
else:

    result = cursor.fetchall()      # 조회된 결과를 튜플로 반환함.

    print(f"[DB 수행 성공]: {db.host_info} {db.user.decode('utf-8')} [{dt.datetime.now()}]", sql)
    print(f"수행 결과 : {result.__len__()}")

    [print(x) for x in result]      # row 도 튜플로 나타남.
finally:
    cursor.close()
    db.close()
    print(f"[DB 접속 종료]: {db.host_info} {db.user.decode('utf-8')} [{dt.datetime.now()}]")


# ☆☆☆
# 2.2.1 DictCursor
print("\n[ 2.2.1 DictCursor ] ──────────────────────────────────────────────────────────────────────────────────────\n")

# 딕셔너리 커서 자체는 모든 쿼리문에 사용 가능하지만, 사실상 select 문 외에 불필요.

sql = '''
SELECT * FROM tb_student WHERE age > %(age)s
'''

params = {"age": 30}

# 재접속
db.connect()

cursor = db.cursor(pymysql.cursors.DictCursor)      # DictCursor 선언

try:
    cursor.execute(sql, params)
except Exception as e:
    cursor.rollback()
    print(f"[SQL 에러]: {e.__traceback__}")
else:

    result = cursor.fetchall()      # 조회된 결과를 각 row 가 딕셔너리로 이루어진 리스트로 반환함.
    print(result, type(result))

    print(f"[DB 수행 성공]: {db.host_info} {db.user.decode('utf-8')} [{dt.datetime.now()}]", sql)
    print(f"수행 결과 : {result.__len__()}")

    print("슬픈 만 30살 이상 아재 목록: ")

    # 각 row 가 딕셔너리 이므로 딕셔너리의 특성을 이용하여 특정 키(컬럼)의 값만 뽑아서 활용하기에 편리.
    for x in result:
        print(x["name"], x)
finally:
    cursor.close()
    db.close()
    print(f"[DB 접속 종료]: {db.host_info} {db.user.decode('utf-8')} [{dt.datetime.now()}]")

