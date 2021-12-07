def counting_sort(A, B, k):
    C = k * [0]
    # Initialiserer et tomt tellearray

    for j in range(len(A) - 1):
        C[A[j]] += 1
    # C[i] inneholder nå antall elementer som er lik i
    # i er sifrene som er inkludert i sorteringen f. eks 0-9
    for i in range(1, k):
        C[i] += C[i-1]
    # C[i] inneholder nå anatall elementer som er mindre enn eller lik i
    print(C)
    for l in range(len(A) - 1, 0, -1):
        B[C[A[l]] - 1] = A[l]
        C[A[l]] -= 1


A = [2, 1, 2, 3, 7, 4, 6, 5, 5]
B = len(A) * [None]
counting_sort(A, B, 8)
print(B)
