from io import StringIO
import sys


class Solution:
    def solve(self, N, M, W):
        dp = [[False] * (M + 1) for _ in range(N + 1)]
        dp[0][0] = True

        for m in range(M):
            for i in range(N):
                if not dp[i][m]:
                    continue
                dp[i + 1][m] = True
                if (m + W[i] <= M):
                    dp[i + 1][m + W[i]] = True

        # for i in range(N):
        #     print(dp[i])
        return "Yes" if dp[N][M] else "No"



def main():
    N, M = list(map(int,input().strip().split()))
    W = list(map(int,input().strip().split()))
    print(Solution().solve(N, M, W))

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
