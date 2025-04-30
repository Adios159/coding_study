import time
import random

mon_hp = 50
ply_hp = 50
turn = 0

print("전투 시작!")
print("플레이어 체력: 50, 몬스터 체력: 50")

while True:
    mon_atk = random.randint(5, 10)
    
    if random.random() < 0.8:
        ply_atk = random.randint(1, 5)
        mon_hp = mon_hp - ply_atk
        print("몬스터의 남은 체력:", mon_hp)
    else:
        ply_atk = random.randint(15, 20)
        mon_hp = mon_hp - ply_atk
        print("몬스터의 남은 체력:", mon_hp)

    ply_hp = ply_hp - mon_atk
    print("플레이어의 남은 체력:", ply_hp)

    time.sleep(1.5)

    if mon_hp <= 0:
        print("플레이어님이 승리했습니다!")
        break
    elif ply_hp <= 0:
        print("몬스터가 승리했습니다...")
        break

    
    
   