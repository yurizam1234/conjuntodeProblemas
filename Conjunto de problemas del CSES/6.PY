t = int(input())
for _ in range(t):
    y, x = map(int, input().split())
    m = max(y, x)
    m2 = m * m

    if m % 2 == 1:  # m impar
        if y == m:
            ans = m2 - x + 1
        else:
            ans = (m - 1) * (m - 1) + y
    else:  # m par
        if x == m:
            ans = m2 - y + 1
        else:
            ans = (m - 1) * (m - 1) + x

    print(ans)
