a = int(input("a: "))
b = int(input("b: "))

if a < 0 or b < 0:
    print("a and b must be > 0") 
elif a < b:
    print(a / b + 5)
elif a == b:
    print(-5)
elif a > b:
    print((a * a - b) / b)
