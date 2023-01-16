def merge(left, right):
    i = 0
    j = 0

    output = []
    while i <= (len(left) - 1) and j <= (len(right) - 1):
        if left[i] < right[j]:
            output.append(left[i])
            i = i + 1
        elif right[j] < left[i]:
            output.append(right[j])
            j = j + 1
        else:
            output.extend([left[i], right[j]])
            i = i + 1
            j = j + 1

    if i == len(left):
        output.extend(right[j:])
    elif j == len(right):
        output.extend(left[i:])

    return output


def mergesort(A):

    n = len(A)

    if n % 2 == 0:
        half_n = n//2
    else:
        half_n = n//2 + 1

    if n <= 1:
        return A
    else:
        left = A[:half_n]
        right = A[half_n:]

        l = mergesort(left)
        r = mergesort(right)
        result = merge(l, r)

    return result

import random
A = random.sample(range(1, 100), 50)

print(mergesort(A))
