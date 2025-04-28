def rotate_list(lst, n):
    if not lst or n == 0:
        return lst

    n = n % len(lst)  
    for _ in range(n):
        lst.insert(0, lst.pop())  
    return lst


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    steps = 2
    rotated_list = rotate_list(my_list, steps)
    print("Rotated List:", rotated_list)