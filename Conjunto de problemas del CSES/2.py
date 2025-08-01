n = int(input())
nums = list(map(int, input().split()))

total = n * (n + 1) // 2  # Suma de 1 a n
suma = sum(nums)

print(total - suma)
