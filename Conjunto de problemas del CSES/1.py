n=int(input())

while True:
    print(n, end="")
    if n == 1:
        break
    elif n % 2 == 0:
        n //= 2
    else:
        n = 3 * n + 1
    print(" ", end="")
    
