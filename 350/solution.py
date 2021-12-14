from io import StringIO
import sys
from collections import defaultdict

class Solution:
    def solve(self, N, MaxW, weights):
        currS = {0: 0}

        # ボールを1つずつ試していく
        for i in range(N):

            # 次の状態の領域
            nextS = defaultdict(lambda: 100000000000)

            # 前の状態が成立するケースのみ試す
            for m in currS:
                # ボールを入れない
                nextS[m] = min(nextS[m], currS[m])

                # ボールを入れられるとき入れる
                if m + W[i] <= M:
                    nextS[m + W[i]] = min(nextS[m + W[i]], currS[m] + 1)

            currS = nextS

        if M in currS:
            # 重さの合計がMになる組み合わせが存在する
            return currS[M]
        else:
            # 組み合わせが存在しない
            return -1

def main():
    N, M = list(map(int, input().strip().split()))
    W = list(map(int, input().strip().split()))
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
