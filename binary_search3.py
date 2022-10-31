def binary_search(in_arr, val):
    start = 0
    end = len(in_arr) - 1
    mid = 0
    
    while start <= end:
        mid = round((start + end) / 2)
        
        if in_arr[mid] < val:
            start = mid + 1
        elif in_arr[mid] > val:
            end = mid - 1
        else:
            return mid
    return -1

test_list = [1,3,9,11,15,19,29,31,33,35,37,39,41,43,45,47,49,51]
test_val1 = 1
test_val2 = 15
test_val3 = 41
test_val4 = 25

print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))
print(binary_search(test_list, test_val3))
print(binary_search(test_list, test_val4))