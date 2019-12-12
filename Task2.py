#Task2

k = int(input())

x = 1
n = k
mod = 0
div = 0
num = 0
prev_num = k
 
while (n*k != k*(10**(x-1)) + n//10):
    
    mod = (prev_num) % 10
    div = (prev_num) // 10
    
    num = (mod*k + div)
    n = n + 10**x*(num % 10)
    
    prev_num = num
    x += 1
 
print(n)