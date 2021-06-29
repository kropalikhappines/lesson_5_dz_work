src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

result = [src[num] for num in range(1, len(src)) if src[num] > src[num -1]]
print(result)



def num_lst(lst):
    res = []
    for i in range(1, len(lst)):
        if lst[i] > lst[i -1]:
            res.append(lst[i])
    print(res)

num_lst(src)
