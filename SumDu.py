n =int(input("Enter size:"))
if n<1 or n> 9:
    print("wrong size")
else:    
    for i in range(1, n + 1):
        num = 1
        for j in range(1, i + 1):
            print(num, end=" ")
            num += 1
        print("")
