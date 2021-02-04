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


# 쿼리 수행함수 - 예제에 코드 반복하는 게 싫어서 만들었습니다. insert 예제에서는 못 썼는데, 여기서는 쓸게요. ...근데 update 예제 딱히 할 게 없네요. ㅠㅠ
# 사용방법      - queryExecute(①커넥션, ②쿼리문, ③쿼리문에 매핑할 인수(optional, 리스트, 튜플, 딕셔너리 형태))
# return        - 결과값으로 rowcount 를 반환합니다.
def queryExecute(__conn, query, values=None):
    if not __conn.open:
        __conn.connect()
    elif type(query) is not str:
        raise TypeError('쿼리는 문자열로 입력해주세요', type(query))

    __cursor = __conn.cursor()

    try:
        __cursor.execute(query, values)
    except Exception as e:
        __cursor.rollback()
        print(f"[SQL 에러]: {e.__traceback__}")
    else:

        __conn.commit()       # commit 하지 않으면 반영되지 않음.

        print(f"[DB 수행 성공]: {__conn.host_info} {__conn.user.decode('utf-8')} [{dt.datetime.now()}]", query)
        print(f"수행 결과 : {__cursor.rowcount}")
    finally:
        __cursor.close()
        __conn.close()
        print(f"[DB 접속 종료]: {__conn.host_info} {__conn.user.decode('utf-8')} [{dt.datetime.now()}]")
        return __cursor.rowcount


# 2.3 데이터 변경
print("\n[ 2.3 데이터 변경 ] ───────────────────────────────────────────────────────────────────────────────────────\n")

db = conn('127.0.0.1', 'chatbot', '0000', 'chatbot', 'utf8')

sql = '''
UPDATE tb_student
   SET name = %(new_name)s
     , age = %(new_age)s
 WHERE id = %(id)s
'''

params = {"new_name": "???", "new_age": 0, "id": 2}

# 함수로 분리함.
queryExecute(db, sql, params)
