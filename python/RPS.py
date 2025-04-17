import random

myhand = input("나의 가위/바위/보 ==> ")

comhand = random.choice(["가위", "바위", "보"])
print("컴퓨터의 가위/바위/보 ==> ", comhand)

if myhand == "가위":
    if comhand == "가위":
        print("비겼습니다. ㅡ.ㅡ")
    elif comhand == "바위":
        print("졌습니다. ㅠㅠ")
    elif comhand == "보":
        print("이겼습니다. ^^")

elif myhand == "바위":
    if comhand == "가위":
        print("이겼습니다. ^^")
    elif comhand == "바위":
        print("비겼습니다. ㅡ.ㅡ")
    elif comhand == "보":
        print("졌습니다. ㅠㅠ")

elif myhand == "보":
    if comhand == "가위":
        print("졌습니다. ㅠㅠ")
    elif comhand == "바위":
        print("이겼습니다. ^^")
    elif comhand == "보":
        print("비겼습니다. ㅡ.ㅡ")

