n = 3
if n >= 1 and n <= 10000000:
    while n != 1:
        print(int(n))
        if n % 2 == 0:
            n = n/2
        else:
            n = 3*n+1
    print(int(n))
else:
    print("no way ")
