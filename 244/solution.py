from io import StringIO
import sys

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()

    count = 0
    for i in range(N - 1):
        L = i + 1
        R = N
        while(L != R):
            mid = (L + R) >> 1
            if (A[i] + A[mid] <= K):
                L = mid + 1
            else:
                R = mid
        if L - i - 1 > 0:
            # print(A[i], A[i + 1: L])
            count += L - i - 1
        else:
            break
    print(count)

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
