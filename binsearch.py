from utility.simple_logger import log_function

@log_function
def binary_search(arr, target, low=0, high=None, _log_depth=1):
    if low < 0:
        raise ValueError('Должен быть положительным!')
    if high is None:
        high = len(arr)
    while low < high:
        middle = (low + high) // 2
        if arr[middle] < target:
            low = middle + 1
        else: 
            high = middle
    return low

@log_function
def binary_search_recursive(arr, target, low=0, high=None, _log_depth=1):
    if high is None: 
        high = len(arr)
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif target < arr[mid]:
        return binary_search_recursive(arr, target, low, mid - 1, _log_depth=_log_depth+1)
    else:
        return binary_search_recursive(arr, target, mid + 1, high, _log_depth=_log_depth+1)

data = [1,2,3,4,5,6,7,8,9,10, 11,12, 13,14,15,16,17,18]
binary_search(data, 7)
print()
binary_search_recursive(data, 7)