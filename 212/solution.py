from io import StringIO
import sys

def particle(A, left, right):
    idxL = left
    idxR = right
    x = A[(left + right) >> 1]

    while(idxL <= idxR):
        while(idxL <= idxR) and (A[idxL] < x):
            idxL += 1
        while(idxR >= idxL) and (A[idxR] > x):
            idxR -= 1
        if (idxL > idxR):
            break
        tmp = A[idxL]
        A[idxL] = A[idxR]
        A[idxR] = tmp
        idxL += 1
        idxR -= 1
    return idxL

def quickSort(A, left, right):
    if (left >= right):
        return
    k = particle(A, left, right)
    quickSort(A, left, k - 1)
    quickSort(A, k, right)

def binarySearch(A, target, left, right):
    if left >= right:
        return left
    mid = (left + right) >> 1
    # print(left, right, "mid = ", mid, "midVal = ", A[mid])
    if A[mid] == target:
        return mid

    if A[mid] > target:
        return binarySearch(A, target, left, mid - 1)
    else:
        return binarySearch(A, target, mid + 1, right)

def countUpMoreThan0(N, A):

    # 練習に、敢えてQuickSortで書いてみる O(NlogN)
    quickSort(A, 0, N - 1)

    # 練習に、バイナリサーチで0を探す O(NlogN)
    pos = binarySearch(A, 0, 0, N)

    while(pos < N) and (A[pos] < 1):
        pos += 1

    return len(A) - pos

def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(countUpMoreThan0(N, A))


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
    test1()
    test2()
