def binaryToDecimal(binary):   
    d, i, n = 0, 0, 0
    while(binary != 0): 
        dec = binary % 10
        d = d + dec * pow(2, i) 
        binary = binary//10
        i += 1
    print(d)     
      
n=int(input())
binaryToDecimal(n)      
