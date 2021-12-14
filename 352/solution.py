from io import StringIO
import sys
from collections import defaultdict

class Solution:
    def solve(self, N, A, B, X):

        # まずは何もカードを持っていない状態からスタート
        currS = {0: True}

        # カードを1枚ずつ試す
        for i in range(N):
            nextS = defaultdict(bool)

            for m in currS:
                # カードを選ばない
                nextS[m] |= currS[m]

                # カードを追加した場合
                tmp = (m + X[i]) % A
                nextS[tmp] |= True

            currS = nextS

        return "Yes" if currS[B] else "No"

def main():
    N, A, B = list(map(int, input().strip().split()))
    X = list(map(int, input().strip().split()))
    print(Solution().solve(N, A, B, X))

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
