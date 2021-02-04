# 파이썬 기초 (+카카오톡 챗봇) 스터디 3주차

# python 데이터베이스
# 3. 프로시저 호출


import datetime as dt
import pymysql


# DB 연결함수
def conn(**knv):
    __db = None
    try:
        __db = pymysql.connect(
            host=knv["host"],
            user=knv["user"],
            password=knv["password"],
            db=knv["schema"],
            charset=knv["charset"]
        )
    except Exception as e:
        print(f"[DB 연결 실패]: [{dt.datetime.now()}] {e}")
    else:
        print(f"[DB 연결 성공]: {__db.host_info} {__db.user.decode('utf-8')} [{dt.datetime.now()}]")
    finally:
        return __db


# 3.1 프로시저 호출
print("\n[ 3.1 프로시저 호출 ] ─────────────────────────────────────────────────────────────────────────────────────\n")

db = conn(host='127.0.0.1', user='chatbot', password='0000', schema='chatbot', charset='utf8')

proc_name = "proc_transfer_std"

params = ("전학생", 20, "국적불명")

cursor = db.cursor()

try:
    cursor.callproc(proc_name, params)  # 인자는 튜플 or 리스트로 전달
except Exception as e:
    cursor.rollback()
    print(f"[PROC 호출 에러]: {e.__traceback__}")
else:

    db.commit()                         # 프로시저에 commit 이 없다면 필요함.

    result = cursor.fetchall()          # 프로시저에 결과가 있을 경우 출력용.

    print(f"[PROC 호출 성공]: {db.host_info} {db.user.decode('utf-8')} [{dt.datetime.now()}]", proc_name)
    print(f"수행 결과 : {result.__len__()}")

    [print(x) for x in result]
finally:
    cursor.close()
    db.close()
    print(f"[DB 접속 종료]: {db.host_info} {db.user.decode('utf-8')} [{dt.datetime.now()}]")


# 개인적으로 프로시저에 OUT 변수 없이 나타났다는 게 굉장히 해괴함. Python 이라기 보다 MySQL 의 특징인 듯...
# 이거 몰라서 계속 OUT 변수에 어떤 타입을 해야 row 출력 가능한지 찾다가 2시간 날림. ㅠㅠ
