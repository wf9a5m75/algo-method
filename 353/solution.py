from io import StringIO
import sys

class Solution:
    def solve(self, N, A):
        M = sum(A)
        dp = [[False] * (M + 1) for _ in range(N + 1)]

        dp[0][0] = True
        for n in range(N):
            for m in range(M + 1):
                if not dp[n][m]:
                    continue
                dp[n + 1][m + A[n]] = True
                dp[n + 1][abs(m - A[n])] = True
        # for i in range(N + 1):
        #     print(dp[i])

        res = 0
        while not dp[N][res]:
            res += 1
        return res


def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(Solution().solve(N, A))

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

def test1():
    test("test1", "input01.txt", "output01.txt")

def test0():
    test("test0", "input00.txt", "output00.txt")

if __name__ == "__main__":
    test0()
    test1()
