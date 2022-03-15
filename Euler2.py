# 피보나치 수열에서 4백만 이하이면서 짝수의 합

sum, i, a, b = 2, 0, 1, 2
c = a+b
while( c < 4000000):    
    a = b
    b = c
    c = a + b
    if (c % 2==0):
        sum += c
    
print(sum)
