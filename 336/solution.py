from io import StringIO
import sys

class Solution:
    def solve(self, N, M, A):
        dp = [[False] * M for _ in range(N)]
        dp[0][0] = True

        for y in range(N - 1):
            for x in range(M):
                if not dp[y][x]:
                    continue

                dp[y + 1][x] = True
                if x + A[y] < M:
                    dp[y + 1][x + A[y]] = True
        ans = 0
        for x in dp[N - 1]:
            ans += 1 if x else 0
        return ans

def main():
    N, M = list(map(int, input().strip().split()))
    A = list(map(int, input().strip().split()))

    print(Solution().solve(N, M, A))

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
