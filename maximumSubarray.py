def max_subarray_sum(arr, k):
    if len(arr) < k:
        return None  

    max_sum = 0
    window_sum = 0

    # Calculate the sum of the first window
    for i in range(k):
        window_sum += arr[i]

    max_sum = window_sum

    # Slide the window
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum



I = [2, 1, 5, 1, 4, 2]
k = 3  
result = max_subarray_sum(I, k)
print("Maximum sum of subarray of length", k, "is:", result)