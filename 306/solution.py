from io import StringIO
import sys


class Solution:
    def solve(self, A, M):
        sizeA = len(A)
        INF = 10**10
        dp = [INF] * sizeA
        dp[0] = 0
        for i in range(1, sizeA):
            for j in range(1, M + 1):
                if (i - j >= 0):
                    # dp[i] にjで辿り着くためには、1つ前がdp[i-j]でなければならない
                    dp[i] = min(dp[i], dp[i-j] + A[i]* j)
        return dp[sizeA - 1]

def main():
    n, m = list(map(int, input().strip().split()))
    A = list(map(int, input().strip().split()))
    print(Solution().solve(A, m))

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
