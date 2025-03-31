for i in range(5):  
    for j in range(5):  
        if (i == 0 or i == 5 - 1 or j == 0 or j == 5 - 1) and not (i == 0 and j == 5 - 1) and not (i == 5 - 1 and j == 5 - 1):  
            print('*', end=' ')  
        else:  
            print(' ', end=' ')  
    print("  ", end='')  # Space between patterns

    for j in range(5):  
        if i == 0 or i == 5 - 1 or j == 0 or j == 5 - 1 and not (i == 1 and j == 5-1) and not (i == 3 and j == 5-1) or i ==2:  
            print('*', end=' ')  
        else:  
            print(' ', end=' ')  
    print("  ", end='')  # Space between patterns

    for j in range(5):  
        if (j==0 and i==0) or (i==2 and j==1) or (i==4 and j==2) or (i==2 and j ==3) or (i==0 and j ==4):  
            print('*', end=' ')  
        else:  
            print(' ', end=' ')  
    print("  ", end='')  # Space between patterns

    for j in range(5):  
        if (j == 0 or j == 4) and i != 0 or (i == 0 or i == 2) and (j > 0 and j < 4):  
            print('*', end=' ')  
        else:  
            print(' ', end=' ')  
            
    print()  # Move to the next row
