from io import StringIO
import sys


def max_heapify(A, x, N):
    k = x
    while(k < N):
        parent = k
        left = 2 * k + 1
        right = left + 1

        largest = parent
        if (left < N) and (A[parent] < A[left]):
            largest = left
        if (right < N) and (A[largest] < A[right]):
            largest = right
        if (largest == parent):
            break
        else:
            A[parent], A[largest] = A[largest], A[parent]
            k = largest
            x -= 1

def build_max_heap(A):
    N = len(A)
    X = (N >> 1) - 1

    for k in range(X, -1, -1):
        max_heapify(A, k, N)
    return A

def heapsort(A, breakPoint):
    A = build_max_heap(A)
    N = len(A)

    for i in range(N - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        max_heapify(A, 0, i)
        if (i == breakPoint):
            print(*A)
    return A

def main():
    N, M = list(map(int, input().split()))
    A = list(map(int, input().split()))

    print(*heapsort(A, M))



def test(testName, inputFile, outputFile):
    capture = StringIO()
    sys.stdin = open(inputFile)
    sys.stdout = capture
    main()
    sys.stdin = sys.__stdin__
    sys.stdout = sys.__stdout__
    results = capture.getvalue().split("\n")


    fAnsFile = open(outputFile)
    i = 0
    passTheTest = True
    lenResults = len(results)
    for ansLine in fAnsFile:
        ansLine = ansLine.strip()
        if ansLine != results[i]:
            results[i] = "-->|" + results[i]
            passTheTest = False
        else:
            results[i] = "   |" + results[i]

        i += 1
        if i == lenResults:
            break
    if ((not passTheTest) or (i + 1 != len(results))):
        print("[{0}] -> fail".format(testName))
        print("\n".join(results))
    else:
        print("[{0}] -> pass".format(testName))

    fAnsFile.close()
    capture.close()

def test2():
    test("test2", "input02.txt", "output02.txt")

def test1():
    test("test1", "input01.txt", "output01.txt")

def test0():
    test("test0", "input00.txt", "output00.txt")

if __name__ == "__main__":
    test0()
    # test1()
    # test2()
