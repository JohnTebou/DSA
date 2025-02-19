A = [2,10,48,19,13,109,20,21,13]

def LinearSearch(A, target):
    index = []
    for i in range(len(A)):
        if A[i] == target:
            index.append(i)
    if (len(index) == 0):
        print("Search Failed.")
    return index

print(LinearSearch(A, 13))
