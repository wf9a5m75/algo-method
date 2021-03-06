from io import StringIO
import sys

class Solution:
    def solve(self, N):
        #------------------------------------------
        # 配るDP : 現在の値を基にして、次の場所の準備をする
        #------------------------------------------
        dp = [[0] * N for _ in range(N)]
        dp[0][0] = 1

        for y in range(N):
            for x in range(N):
                if y + 1 < N:
                    dp[y + 1][x] += dp[y][x]

                if x + 1 < N:
                    dp[y][x + 1] += dp[y][x]

        for y in range(N):
            print(dp[y])
        return dp[N - 1][N - 1]

    def solve_dp1(self, N):
        #------------------------------------------
        # 貰うDP : 現在の場所に必要な値を前回の場所から貰う
        #------------------------------------------

        # 1
        #
        # 1 1
        # 1 2
        #
        # 1 1 1
        # 1 2 3
        # 1 3 6
        dp = [[0] * N for _ in range(N)]


        for i in range(N):
            dp[i][0] = dp[0][i] = 1

        for y in range(1, N):
            for x in range(1, N):
                dp[y][x] = dp[y - 1][x] + dp[y][x - 1]

        # for y in range(N):
        #     print(dp[y])
        return dp[N - 1][N - 1]

def main():
    N = int(input())
    print(Solution().solve(N))

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
