from random import randint as rnd

def Quicksort(A, l, r):
    if l >= r:
        return A
    else:
        i = ChoosePivot(l, r)
        first_elem = A[l]
        A[l] = A[i]
        A[i] = first_elem
        j = Partition(A, l, r)
        Quicksort(A, l, j)
        Quicksort(A, j + 1, r)

def ChoosePivot(l, r):
    pivot = rnd(l, r)
    return pivot

def Partition(A, l, r):
    pivot = A[l]
    i = l + 1
    for j in range(l+1,r+1):
        if A[j] < pivot:
            swap_elem = A[j]
            A[j] = A[i]
            A[i] = swap_elem
            i += 1
    swap_elem = A[i-1]
    A[i-1] = A[l]
    A[l] = swap_elem
    return i - 1

A = [100,15,28,34,55,80,1008]
Quicksort(A,0,len(A)-1)
print(A)
