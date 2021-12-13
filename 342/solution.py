from io import StringIO
import sys
from collections import defaultdict

class Solution:
    def solve(self, N, M, weights, values):

        currS = {0: 0}

        # ボールを1つずつ試す
        for i in range(N):
            nextS = defaultdict(int)
            # 前の状態が成立するケースだけを試す
            for m in currS:

                # ボールを入れなかったとき
                nextS[m] = max(nextS[m], currS[m])

                # ボールを入れても合計がM以下の場合
                if m + A[i] <= M:
                    nextS[m + A[i]] = max(nextS[m + A[i]], currS[m] + B[i])

            #print(*nextS)

            # 現在の状態を次の状態とする
            currS = nextS

        # 最大値を返す
        maxW = 0
        for m in currS:
            maxW = max(maxW, currS[m])
        return maxW


def main():
    N, M = list(map(int, input().strip().split()))
    A = list(map(int, input().strip().split()))
    B = list(map(int, input().strip().split()))
    print(Solution().solve(N, M, A, B))


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
