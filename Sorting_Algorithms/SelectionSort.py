A = [2, 10, 48, 19, 13, 109, 20, 21]
B = [100, 99, 98, 97, 30, 29, 28, 16, 12, 10, 8, 2]
C = [100, 100, 99, 98, 97, 30, 29, 28, 16, 12, 10,90, 8, 2, 98]


def SelectionSort(A):
    n = len(A)
    for i in range(n-1):
        tempMin = A[i]
        targIndex = i
        for j in range(i+1, n):
            if A[j] < tempMin:
                tempMin = A[j]
                targIndex = j
        A[targIndex] = A[i]
        A[i] = tempMin
    return A


print(SelectionSort(A))
print(SelectionSort(B))
print(SelectionSort(C))
