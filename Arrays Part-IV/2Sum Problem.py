def pairSum(arr, s):
    hs = set()
    res = []
    for i in arr:
        hs.add(i)
        req = s - i
        if req in hs:
            res.append([i, req])
        print(i, hs)
    return res

s = 4
arr = {2, -6, 2, 5, 2}
print(pairSum(arr, s))


        
            