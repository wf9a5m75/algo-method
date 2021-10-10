from io import StringIO
import sys

class Solution:
    def solve(self, S):
        N = len(S)
        for i in range(N):
            S[i] = list(S[i])

        dp = [[0] * N for _ in range(N)]
        dp[0][0] = 1
        for y in range(N):
            for x in range(N):
                if (y + 1 < N) and (S[y + 1][x] != "#"):
                    dp[y + 1][x] += dp[y][x]

                if (x + 1 < N) and (S[y][x + 1] != "#"):
                    dp[y][x + 1] += dp[y][x]
        return dp[N - 1][N - 1]



def main():
    N = int(input())
    S = []
    for _ in range(N):
        S.append(input().strip())
    print(Solution().solve(S))

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
