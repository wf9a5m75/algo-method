from io import StringIO
import sys

class Solution:
    def solve(self, A):
        INF = 1000000
        N = len(A)
        N1 = N + 1
        dp = [[INF] * N for i in range(N)]
        dp[0][N - 1] = A[0][N - 1]

        for x in range(N - 1, -1, -1):
            for y in range(N ):
                if x - 1 >= 0:
                    dp[y][x - 1] = min(dp[y][x - 1], dp[y][x] + A[y][x - 1])

                if y + 1 < N:
                    dp[y + 1][x] = min(dp[y + 1][x], dp[y][x] + A[y + 1][x])

        return dp[N - 1][0]

def main():
    N = int(input())
    A = []
    for _ in range(N):
        A.append(list(map(int, input().strip().split())))

    print(Solution().solve(A))

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
