def quikcsort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quikcsort(A, p, q - 1)
        quikcsort(A, q + 1, r)


def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i = i + 1
            ex1 = A[j]
            ex2 = A[i]
            A[i] = ex1
            A[j] = ex2
    ex1 = A[r]
    ex2 = A[i + 1]
    A[i + 1] = ex1
    A[r] = ex2
    return i + 1


A = [1, 5, 4, 2, 8, 10, 12, 6, 4, 3, 2, 3, 19, 28, 17, 5]
quikcsort(A, 0, len(A) - 1)
print(A)
