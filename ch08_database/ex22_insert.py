# 파이썬 기초 (+카카오톡 챗봇) 스터디 3주차

# python 데이터베이스
# 2. CRUD


import datetime as dt
import pymysql


# DB 연결함수
def conn(host, user, password, schema=None, charset='utf8'):
    db = None
    try:
        db = pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=schema,
            charset=charset
        )
    except Exception as e:
        print(f"[DB 연결 실패]: [{dt.datetime.now()}] {e}")
    else:
        print(f"[DB 연결 성공]: {db.host_info} {db.user.decode('utf-8')} [{dt.datetime.now()}]")
    finally:
        return db


# # 쿼리 수행함수 - 예제에 코드 반복하는 게 싫어서 만들었는데, 처음 개념을 잡는 것이므로 주석처리하고 귀찮아도 다 쓰기로 했습니다.
# # 사용방법      - queryExecute(①커넥션, ②쿼리문, ③쿼리문에 매핑할 인수(optional, 리스트, 튜플, 딕셔너리 형태))
# # return        - 결과값으로 rowcount 를 반환합니다.
# def queryExecute(conn, query, values=None):
#     if not conn.open:
#         conn.connect()
#     elif type(query) is not str:
#         raise TypeError('쿼리는 문자열로 입력해주세요', type(query))
#
#     cursor = conn.cursor()
#
#     try:
#         cursor.execute(query, values)
#     except Exception as e:
#         cursor.rollback()
#         print(f"[SQL 에러]: {e.__traceback__}")
#     else:
#
#         conn.commit()       # commit 하지 않으면 반영되지 않음.
#
#         print(f"[DB 수행 성공]: {conn.host_info} {conn.user.decode('utf-8')} [{dt.datetime.now()}]", query)
#         print(f"수행 결과 : {cursor.rowcount}")
#     finally:
#         cursor.close()
#         conn.close()
#         print(f"[DB 접속 종료]: {conn.host_info} {conn.user.decode('utf-8')} [{dt.datetime.now()}]")
#         return cursor.rowcount


# 2.1 데이터 삽입
print("\n[ 2.1 데이터 삽입 ] ───────────────────────────────────────────────────────────────────────────────────────\n")

# 함수로 따로 분리함.
db = conn('127.0.0.1', 'chatbot', '0000', 'chatbot', 'utf8')


sql = '''
INSERT INTO tb_student(name, age, address) VALUES('홍길동', 35, '대한민국')
'''

cursor = db.cursor()

try:
    cursor.execute(sql)
except Exception as e:
    cursor.rollback()
    print(f"[SQL 에러]: {e.__traceback__}")
else:

    db.commit()     # commit 하지 않으면 결과가 반영되지 않음.

    print(f"[DB 수행 성공]: {db.host_info} {db.user.decode('utf-8')} [{dt.datetime.now()}]", sql)
    print(f"수행 결과 : {cursor.rowcount}")
finally:
    cursor.close()
    db.close()
    print(f"[DB 접속 종료]: {db.host_info} {db.user.decode('utf-8')} [{dt.datetime.now()}]")


# ☆☆☆
# 2.1.1 쿼리문 매개변수 매핑
print("\n[ 2.1.1 쿼리문 매개변수 매핑 ] ────────────────────────────────────────────────────────────────────────────\n")

# 보통 sql 문을 직접 다 쓰지는 않고 변수와 함께 포맷팅 해서 사용함.

a = "아리랑"
b = 18
c = "대한민국"

sql = '''
INSERT INTO tb_student(name, age, address) VALUES('%s', %d, '%s')
''' % (a, b, c)

# 작은 따옴표(')에 주의.

# 재접속
db.connect()

cursor = db.cursor()

try:
    cursor.execute(sql)
except Exception as e:
    cursor.rollback()
    print(f"[SQL 에러]: {e.__traceback__}")
else:

    db.commit()     # commit 하지 않으면 결과가 반영되지 않음.

    print(f"[DB 수행 성공]: {db.host_info} {db.user.decode('utf-8')} [{dt.datetime.now()}]", sql)
    print(f"수행 결과 : {cursor.rowcount}")
finally:
    cursor.close()
    db.close()
    print(f"[DB 접속 종료]: {db.host_info} {db.user.decode('utf-8')} [{dt.datetime.now()}]")


# 이렇게, 매핑해서 많이 활용. ("처음 배우는 딥러닝 챗봇" 교재도 이렇게 소개하고 있음.)
# 그러나, SQL Injection 공격에 취약한 Bad Case.

# 따라서, 아래처럼 할 것을 권장하고 있음.
print("\n# SQL Injection 방지")

a = "아리랑"
b = 18
c = "대한민국"

sql = '''
INSERT INTO tb_student(name, age, address) VALUES(%s, %s, %s)
'''

# 작은 따옴표(') 없음. 변수의 타입에 상관없이 %s 키워드로만 매핑됨.

# 재접속
db.connect()

cursor = db.cursor()

try:
    cursor.execute(sql, (a, b, c))     # execute() 함수에 튜플, 리스트 등으로 전달.
except Exception as e:
    cursor.rollback()
    print(f"[SQL 에러]: {e.__traceback__}")
else:

    db.commit()

    print(f"[DB 수행 성공]: {db.host_info} {db.user.decode('utf-8')} [{dt.datetime.now()}]", sql)
    print(f"수행 결과 : {cursor.rowcount}")
finally:
    cursor.close()
    db.close()
    print(f"[DB 접속 종료]: {db.host_info} {db.user.decode('utf-8')} [{dt.datetime.now()}]")

# PyMySQL 모듈 내부에서 각각 sql 문과 인자를 매핑하여 쿼리를 수행함.
# 이렇게 할 것을 권장하고 있으므로 참조.

# 같은 이유로, format 함수나 f-string 역시 취약함.

# 그러나 Java 에서 사용하는 PreparedStatement 만큼 강력한 방어 기능을 제공하는 것 같진 않으므로 확인 필요.

# 딕셔너리 매핑
print("\n# 딕셔너리 매핑")

params = {"name": "아무개", "age": 38, "address": "대한민국"}

sql = '''
INSERT INTO tb_student(name, age, address) VALUES(%(name)s, %(age)s, %(address)s)
'''

# %(키 이름)s 형태로 딕셔너리와 매핑 가능. %()s 안에는 따옴표없이 입력해야 함.

# 재접속
db.connect()

cursor = db.cursor()

try:
    cursor.execute(sql, params)
except Exception as e:
    cursor.rollback()
    print(f"[SQL 에러]: {e.__traceback__}")
else:

    db.commit()

    print(f"[DB 수행 성공]: {db.host_info} {db.user.decode('utf-8')} [{dt.datetime.now()}]", sql)
    print(f"수행 결과 : {cursor.rowcount}")
finally:
    cursor.close()
    db.close()
    print(f"[DB 접속 종료]: {db.host_info} {db.user.decode('utf-8')} [{dt.datetime.now()}]")


# 사실상, 딕셔너리 매핑 형태를 가장 많이 활용함.


# 2.1.2 쿼리문 반복 실행
print("\n[ 2.1.2 쿼리문 반복 실행 ] ────────────────────────────────────────────────────────────────────────────────\n")

# executemany(sql, params_list): 동일한 sql 문을 params_list 의 길이만큼 반복수행 하는 함수.
print("\n# executemany()")


sql = '''
INSERT INTO tb_student(name, age, address) VALUES(%s, %s, %s)
'''

params_list = [
    ('Peter', 18, 'Lowstreet 4'),
    ('Amy', 15, 'Apple st 652'),
    ('Hannah', 16, 'Mountain 21'),
    ('Michael', 21,'Valley 345'),
    ('Sandy', 17, 'Ocean blvd 2'),
    ('Betty', 15, 'Green Grass 1'),
    ('Richard', 32, 'Sky st 331'),
    ('Susan', 24,'One way 98'),
    ('Vicky', 20, 'Yellow Garden 2'),
    ('Ben', 26, 'Park Lane 38'),
    ('William', 27, 'Central st 954'),
    ('Chuck', 41, 'Main Road 989'),
    ('Viola', 23, 'Sideway 1633')
]

# 재접속
db.connect()

cursor = db.cursor()

try:
    cursor.executemany(sql, params_list)
except Exception as e:
    cursor.rollback()
    print(f"[SQL 에러]: {e.__traceback__}")
else:

    db.commit()

    print(f"[DB 수행 성공]: {db.host_info} {db.user.decode('utf-8')} [{dt.datetime.now()}]", sql)
    print(f"수행 결과 : {cursor.rowcount}")
finally:
    cursor.close()
    db.close()
    print(f"[DB 접속 종료]: {db.host_info} {db.user.decode('utf-8')} [{dt.datetime.now()}]")


# executemany() 함수 역시 내부적으로는 for 반복문으로 수행되기 때문에,
# execute() 함수를 반복문으로 반복 실행하는 것과 성능적으로 어떤 차이가 있는지는 확인이 필요.

# 결국, batch 로 동작하는 건 아니므로, 얼마나 많은 양의 데이터를 수행할 수 있는지도 확인이 필요.
