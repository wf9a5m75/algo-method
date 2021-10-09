from io import StringIO
import sys

class Solution:
    def solve(self, N):
        if (N < 1):
            return 0
        if (N == 1):
            return 1

        # 1 -> 1
        # 2 -> 1-1, 2
        # 3 -> 1-1-1, 1-2, 2-1
        # 4 -> 1-1-1-1, 1-1-2, 1-2-1, 2-1-1, 2-2
        # n -> dp[n - 2] + dp[n - 1] => dp[n + 2] = dp[n] + dp[n + 1]
        dp = [0] * (N + 1)
        dp[1] = 1
        dp[2] = 2
        for i in range(1, N - 2 + 1):
            dp[i + 2] = dp[i] + dp[i + 1]
        return dp[N]


def main():
    n = int(input())
    print(Solution().solve(n))

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
