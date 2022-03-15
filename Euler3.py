# 600851475143의 소인수들 중 가장 큰 수

n = 600851475143
result = []
for i in range(2,n):
    if n % i == 0:
        result = i
        n = n/i
        if n % i == 1:
            break

print(result)