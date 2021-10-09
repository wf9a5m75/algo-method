from io import StringIO
import sys


class Solution:
    def solve(self, A, N):
        sizeA = len(A)
        dp = [False] * (N + 1)
        dp[0] = True
        for i in range(1, N + 1):
            for j in range(0, sizeA):
                if (i - A[j] >= 0) and dp[i-A[j]]:
                    dp[i] = True
        return 'Yes' if dp[N] else 'No'

def main():
    n, m = list(map(int, input().strip().split()))
    A = list(map(int, input().strip().split()))
    print(Solution().solve(A, n))

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
    # test2()
