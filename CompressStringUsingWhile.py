def compress_string(s):
    compressed = ""
    i = 0
    while i < len(s):
        c1 = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            c1 += 1
            i += 1
        compressed += s[i] + str(c1)
        i += 1
    return compressed if len(compressed) < len(s) else s


input_string = input("Enter a String : ")
result = compress_string(input_string)
print(f"Compressed string: {result}")