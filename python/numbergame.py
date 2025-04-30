import random 

com_num = random.randint(1, 100)
count = 0

print("1부터 100까지의 수를 맞혀보세요!")

while True:
    ply_num = int(input("숫자를 입력하세요: "))
    count += 1

    if ply_num < com_num:
        print("더 큽니다!")
    elif ply_num > com_num:
        print("더 작습니다!")
    else:
        print("정답입니다!")
        print("총", count, "번 만에 맞추셨습니다!")
        break