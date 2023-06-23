def mergeSort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        n1 = mid - left + 1
        n2 = right - mid
        left_arr = [0 for i in range(n1)]
        right_arr = [0 for i in range(n2)]
        temp = [0 for i in range(n1 + n2)]
        i, j, k = left, mid, 0
        while i < mid and j <= right:
            if arr[i] <= arr[j]:
                
            






arr = [3, 2, 1]
temp = [0 for i in range(len(arr))] 
mergeSort(arr, 0, len(arr) - 1)
print(arr)






# def mergeSort(arr, temp, left, right):
#     inv_count = 0
#     if left < right:
#         mid = (left + right) // 2
#         inv_count += mergeSort(arr, temp, left, mid)
#         inv_count += mergeSort(arr, temp, mid + 1, right)
#         inv_count += merge(arr, temp, left, mid, right)
#     return inv_count

# def merge(arr, temp, left, mid, right):
#     i = left
#     j = mid + 1
#     k = left
#     inv_count = 0
#     while i <= mid and j <= right:
#         if arr[i] <= arr[j]:
#             temp[k] = arr[i]
#             k += 1
#             i += 1
#         else:
#             temp[k] = arr[j]
#             k += 1
#             j += 1
#             inv_count += (mid - i + 1)
#     while i <= mid:
#         temp[k] = arr[i]
#         k += 1
#         i += 1
#     while j <= right:
#         temp[k] = arr[j]
#         k += 1
#         j += 1
#     for loop_var in range(left, right + 1):
#         arr[loop_var] = temp[loop_var]
#     return inv_count

# def inversionCount(arr, n):
#     temp = [0] * n
#     return mergeSort(arr, temp, 0, n - 1)


