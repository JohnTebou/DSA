import math

A = [5, 6, 7, 8, 9, 1, 2, 3, 4]
B = [100, 99, 98, 97, 30, 29, 28, 16, 12, 10, 8, 2]


def Merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L, R = [], []
    for m in range(n1):
        L.append(A[p + m])
    for n in range(n2):
        R.append(A[q + 1 + n])
    i = 0
    j = 0
    k = p
    while i < n1 and j < n2:
        if L[i] < R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        A[k] = L[i]
        k += 1
        i += 1
    while j < n2:
        A[k] = R[j]
        k += 1
        j += 1


def MergeSort(A, p, r):
    if p >= r:
        return
    q = math.floor((p + r) / 2)
    MergeSort(A, p, q)
    MergeSort(A, q + 1, r)
    Merge(A, p, q, r)


Merge(A, 0, 4, len(A) - 1)
MergeSort(B, 0, len(B) - 1)

print(A)
print(B)
