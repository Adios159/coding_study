def test(a, b=10, c=100):
    print(a + b + c)

test(10, 20, 30)
test(a=10, b=100, c=200)
test(c=10, b=100, a=200)
test(10, c=200)