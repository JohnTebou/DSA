A = [2,10,48,19,13,109,20,21]
B = [100, 99, 98, 97, 30, 29, 28, 16, 12, 10, 8, 2]

def InsertionSort(A):
    for i in range(1, len(A)):
        key = A[i]
        j = i-1
        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key
    return A

print(InsertionSort(A))
print(InsertionSort(B))