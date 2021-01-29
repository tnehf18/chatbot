# sub_md.py
"""
ex15_module.py 모듈 예제용 파일
"""


def showMd():
    print("모듈입니다.")


def showName():
    if __name__ == "__main__":
        print("현재 파일에서 실행되었습니다.", __name__)
    else:
        print("모듈로 import 되었습니다.", __name__)


if __name__ == "__main__":
    showName()

