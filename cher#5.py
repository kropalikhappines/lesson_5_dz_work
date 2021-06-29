src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
uniq_num = set()
tmp = set()
for el in src:
    if el not in tmp:
        uniq_num.add(el)
    else:
        uniq_num.discard(el)
    tmp.add(el)
    uniq_num_2 = [ele for ele in src if ele in uniq_num]
print(uniq_num_2)

