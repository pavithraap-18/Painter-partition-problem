def is_possible(arr, n, k, max_time):
    painter_count = 1
    current_sum = 0

    for i in range(n):
        if arr[i] > max_time:
            return False  # A single board exceeds the limit

        if current_sum + arr[i] > max_time:
            painter_count += 1
            current_sum = arr[i]
            if painter_count > k:
                return False
        else:
            current_sum += arr[i]

    return True

def painters_partition(arr, k):
    n = len(arr)
    low = max(arr)
    high = sum(arr)
    result = high

    while low <= high:
        mid = (low + high) // 2
        if is_possible(arr, n, k, mid):
            result = mid
            high = mid - 1
        else:
            low = mid + 1

    return result
