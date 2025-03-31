a = int(input("Enter a number : "))
sum = 0
b= a
while b>0:
    sum += b%10
    b = b//10
    

if a%sum==0: 
    print("It is Harshad number")
else: 
    print('It is not') 
    