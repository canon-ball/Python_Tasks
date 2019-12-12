# Task1

import math

digits = 0 #amount of digits
n = int(input())
temp = n
ispal = False #flag ispalindrom

if n%10 == 0:
    print('NO')
else:
    while temp!=0:
        temp //= 10
        digits += 1
    for i in range(math.ceil(digits/2)):
        if (n//10**i % 10) != (n//10**(digits-1-i) % 10):
            ispal = False
            break
        else:
            ispal = True
        
if ispal is True:
    print('YES')
else:
    print('NO')