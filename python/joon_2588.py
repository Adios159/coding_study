A = int(input())
B = int(input())

b1 = A * (B // 100)
b2 = A * ((B // 10) % 10)
b3 = A * (B % 10)

C = A * B

print(b1)
print(b2)
print(b3)
print(C)
