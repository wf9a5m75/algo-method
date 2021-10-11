from io import StringIO
import sys

# 文字列　S1の中に 文字列 S2 が含まれるかどうかを、DPを使って解いてみる
class Solution:
    def solve(self, S1, S2):

        S1 = list(S1)
        S2 = list(S2)
        N1 = len(S1)
        N2 = len(S2)

        dp = [[0] * (N2 + 1) for _ in range(N1 + 1)]

        for i in range(N1):
            for j in range(N2):
                if S1[i] == S2[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1

        # for i in range(N1):
        #     print(dp[i])
        for i in range(N1):
            if dp[i][N2] == N2:
                return "Yes"
        return "No"


def main():
    S1 = input().strip()
    S2 = input().strip()

    print(Solution().solve(S1, S2))

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
