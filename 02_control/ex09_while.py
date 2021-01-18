# 2.1 while 문

i = 1
while i < 6:
    print(i)
    i += 1

# break
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

# else
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i 가 6 보다 작지 않습니다.")

# do ~ while 문은 존재하지 않으나, 다음과 같이 할 수 있음.

i = 1
while True:
    print(i)
    i += 1
    if i < 6:
        continue
    else:
        break
