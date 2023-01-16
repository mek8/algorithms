def merge(left, right):
    i = 0
    j = 0
    sp_inv = 0
    output = []
    while i <= (len(left) - 1) and j <= (len(right) - 1):
        if left[i] < right[j]:
            output.append(left[i])
            i = i + 1
        elif right[j] < left[i]:
            output.append(right[j])
            j = j + 1
            sp_inv = sp_inv + len(left[i:])
        else:
            output.extend([left[i], right[j]])
            i = i + 1
            sp_inv = sp_inv + len(left[i:])
            if right[j] in left[i:]:
                minus = left[i:].count(right[j])
                sp_inv = sp_inv - minus
            j = j + 1



    if i == len(left):
        output.extend(right[j:])
    elif j == len(right):
        output.extend(left[i:])

    return output, sp_inv


def mergesort(A):

    n = len(A)

    if n % 2 == 0:
        half_n = n//2
    else:
        half_n = n//2 + 1

    if n <= 1:
        inv = 0
        return A, inv
    else:
        left = A[:half_n]
        right = A[half_n:]

        l, l_inv = mergesort(left)
        r, r_inv = mergesort(right)
        array, sp_inv = merge(l, r)
        inv = l_inv + r_inv + sp_inv

    return array, inv

#import random
#A = random.sample(range(1, 100), 50)
A = [1,1,2,1,1,4,6,1]
print(mergesort(A))
