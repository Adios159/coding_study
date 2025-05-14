import random

comNum = random.randint(1, 5)
playtime = 1

while playtime <= 10:
    plyNum = int(input(f"게임 {playtime}회: 컴퓨터가 생각한 숫자는? "))

    if comNum == plyNum:
        print("맞혔네요. 축하합니다!!")
        break
    else:
        print(f"아까워요. 정답은 {comNum} 이었어요... ㅠㅠ")
        comNum = random.randint(1, 5)
    playtime += 1

if playtime > 10:
    print("10번의 기회를 모두 사용하셨습니다.")