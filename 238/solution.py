from io import StringIO
import sys

def binarySearch(A, target, left, right):
    while(left != right):
        mid = (left + right) >> 1
        if A[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left


def main():

    L, R = list(map(int, input().split()))

    cnt = 0
    # 1-9
    if (1 <= L <= min(9, R)):
        cnt += min(9, R) - L + 1

    # xx => x = [1..9]
    if (R > 9):
        A = [11, 22, 33, 44, 55, 66, 77, 88, 99]


        # x(0-9)x * 9 => x = [1..9]
        if (R <= 999):
            for x in range(1, 10):
                bias = x * 100 + x
                for y in range(0, 10):
                    n = bias + y * 10
                    A.append(n)
        sizeA = len(A)
        posL = binarySearch(A, L, 0, sizeA)
        if (A[posL] < L):
            posL += 1
        posR = binarySearch(A, R, 0, sizeA)
        # print(posR, A[posR])
        if (posR < sizeA) and (A[posR] == R):
            posR += 1
        cnt += posR - posL

        # print(A)

    print(cnt)

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
