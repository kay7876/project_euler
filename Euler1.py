# 1000보다 작은 자연수 중 3 또는 5의 배수의 합

sum = 0

for i in range(0, 1000) :
    if i % 3 == 0 or i % 5 == 0 : sum += i
    
print(sum)