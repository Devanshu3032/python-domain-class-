# Define the patterns for each letter
def print_D():
    for i in range(5):
        for j in range(5):
            if j == 0 or (i == 0 or i == 4) and j < 4 or (j == 4 and i != 0 and i != 4):
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()

def print_E():
    for i in range(5):
        for j in range(5):
            if j == 0 or i == 0 or i == 2 or i == 4:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()

def print_V():
    for i in range(5):
        for j in range(9):
            if j == i or j == 8 - i:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()

# Call the functions for each letter
print_D()
print()
print_E()
print()
print_V()
