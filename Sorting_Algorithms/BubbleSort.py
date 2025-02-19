A = [2, 10, 48, 19, 13, 109, 20, 21]
B = [100, 99, 98, 97, 30, 29, 28, 16, 12, 10, 8, 2]
C = [100, 100, 99, 98, 97, 30, 29, 28, 16, 12, 10, 90, 8, 2, 98]


def BubbleSort(A):
    for i in range(len(A) - 1):
        for j in range(len(A) - 1, i, -1):
            if A[j] < A[j - 1]:
                a = A[j]
                b = A[j - 1]
                A[j], A[j - 1] = b, a
    return A


print(BubbleSort(A))
print(BubbleSort(B))
print(BubbleSort(C))
