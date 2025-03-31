a = int(input("Enter a number : "))
b = a 
product =1 
c = False
while b > 0:
    rem = b%10
    product *= rem
    if product== 0 :
        c = True
    else: 
        c = False
print(c) 
        