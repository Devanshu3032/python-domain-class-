def max_subarray_sum(arr, k):
    if len(arr) < k:
        return None  # Not enough elements for the subarray

    max_sum = 0
    window_sum = 0

    # Calculate the sum of the first window
    for i in range(k):
        window_sum += arr[i]

    max_sum = window_sum

I = [2, 1, 5, 1, 3, 2]
k = 3  # Length of the subarray
result = max_subarray_sum(I, k)
print("Maximum sum of subarray of length", k, "is:", result)