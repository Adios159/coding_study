hap = 0
num1, num2 = 0, 0

while True:
    num1 = int(input("첫번째 숫자를 입력하세요 ==> "))
    if num1 == 0:
        print("0을 입력하였으므로 프로그램을 종료합니다.")
        break
    
    
    num2 = int(input("두번째 숫자를 입력하세요 ==> "))


    hap = num1 + num2
    print(num1, "+", num2, "=", hap)