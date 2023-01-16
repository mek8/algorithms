def count_inverstions_and_sort(array1, array2):
    res = []
    num_inv = 0
    i = 0
    j = 0
    l1 = len(array1)
    l2 = len(array2)

    for _ in range(l1 + l2):
        if i == l1:
            res += [array2[x] for x in range(j, l2)]
            break
        if j == l2:
            res += [array1[x] for x in range(i, l1)]
            break
        if array1[i] < array2[j]:
            res.append(array1[i])
            i += 1
        else:
            res.append(array2[j])
            j += 1
            num_inv += (l1 - i)
    return (num_inv, res)

def sort_and_count(array):
    if len(array) == 1:
        return (0, array)

    i = len(array)//2
    l_inv, left = sort_and_count(array[0:i])
    r_inv, right = sort_and_count(array[i:])
    split_inv, merged = count_inverstions_and_sort(left, right)
    return (l_inv + r_inv + split_inv, merged)

A = [1,1,2,1,1,4,6,1]
print(sort_and_count(A))
