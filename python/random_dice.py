import random

count = 0
dice1, dice2, dice3, dice4 = 0, 0, 0, 0

while True:
    count += 1
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice3 = random.randint(1,6)
    dice4 = random.randint(1,6)

    if (dice1 == dice2) and (dice2 == dice3) and (dice3 == dice4):
        break

print("3개 주사위 모두", dice1, "이 나왔습니다")
print("같은 숫자가 나오기까지", count, "번 던졌습니다")