a = int(input("Enter a number : "))
sum = 0
product = 1
c = False
b = a 
while b > 0: 
    rem = b%10
    sum += rem
    product *= rem
    b = b//10
    
    if sum == product:
        c =  True
        
        
    else:
        c = False
        
print(c)
