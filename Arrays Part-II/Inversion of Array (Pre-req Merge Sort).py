def merge(arr, low, mid, high):
    temp = []
    left = low
    right = mid + 1
    count = 0
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            if arr[left] > 2*arr[right]:
                count += mid - left + 1
            temp.append(arr[right])
            right += 1
    while left <= mid:
        temp.append(arr[left])
        left += 1
    while right <= high:
        temp.append(arr[right])
        right += 1
    for i in range(high - low + 1):
        arr[low + i] = temp[i]
    return count

def mergeSort(arr, low, high):
    count = 0
    if low < high:
        mid = (low + high) // 2
        count += mergeSort(arr, low, mid)
        count += mergeSort(arr, mid + 1, high)
        count += merge(arr, low, mid, high)
    return count

arr = [5, 4, 3, 2, 1, 1, 1]
print(arr)
print(mergeSort(arr, 0, len(arr) - 1))
print(arr)