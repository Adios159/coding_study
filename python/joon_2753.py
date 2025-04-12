year = int(input("숫자 입력:")) 
a = 1
b = 0

if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
    print(a)
else:
    print(b)