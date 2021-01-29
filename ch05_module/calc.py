# calc.py
"""
ex15_module.py 모듈 예제용 파일
"""


# 덧셈
def add(a, b): return a + b


# 뺄셈
def sub(a, b): return a - b


# 곱셈
def mul(a, b): return a * b


# 나눗셈
def div(a, b): return a / b


class Formatter:

    def comma(value):
        return f"{value:20,.2f}"
