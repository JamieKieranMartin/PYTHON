def SeqSearch(A, K):
    i = 0
    while i < len(A) and A[i] is not K:
        i = i + 1
    if i < len(A):
        return i
    else:
        return -1

if __name__ == "__main__":
    print(SeqSearch([5,2,4,3], 10))