#세자리 수를 곱해서 만들 수 있는 가장 큰 대칭수

for i in range(900, 999):
    for j in range (900, 999):
        result = str(i * j)
                
        if result == result[::-1]:
                 print(result , i, j)