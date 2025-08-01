n = int(input())

if n == 1:
    print(1)
elif n in (2, 3):
    print("NO HAY SOLUCIÓN")
else:
    pares = [str(i) for i in range(2, n+1, 2)]
    impares = [str(i) for i in range(1, n+1, 2)]
    print(" ".join(pares + impares))
