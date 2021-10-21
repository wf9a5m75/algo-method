from io import StringIO
import sys


def heapify(A):
    N = len(A)
    x = (N >> 1) - 1

    while (x >= 0):

        k = x
        while(k < N):
            parent = k
            left  = 2 * k + 1
            right = 2 * k + 2

            largest = parent

            if (left < N) and (A[k] < A[left]):
                largest = left

            if (right < N) and (A[largest] < A[right]):
                largest = right

            if (largest != parent):
                A[parent], A[largest] = A[largest], A[parent]
                k = largest
            else:
                break
        x -= 1
    return A

def main():

    N = int(input())
    A = list(map(int, input().split()))
    print(*heapify(A))



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
