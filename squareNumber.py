a = int(input("Enter a number : "))
square = a * a

# Convert the square to a string and check if the string of 'a' is in it
if str(a) in str(square):
    print("Yes")
else:
    print("No")  