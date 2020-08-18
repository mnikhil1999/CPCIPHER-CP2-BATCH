n = int(input())
def count_digit(n):
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count
 
def isArmstrong (x): 
    n = count_digit(x) 
    temp = x 
    sum1 = 0
    while (temp!=0): 
        r = temp%10
        sum1 = sum1 + (r**n)
        temp = temp/10
        
    return (sum1 == x)
print(isArmstrong(n))
