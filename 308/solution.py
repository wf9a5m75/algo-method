from io import StringIO
import sys

def main():
    N, W = list(map(int, input().split()))

    # 何もない状態からスタート
    currS = {0: 0}

    for i in range(N):
        nextS = {}
        w, v = list(map(int, input().split()))

        for prevW in currS:
            # w(i) を足さない
            nextS[prevW] = max(nextS.get(prevW) or 0, currS[prevW])

            # w(i) を加えてもW以下の場合は足す
            if prevW + w <= W:
                nextS[prevW + w] = max(nextS.get(prevW + w) or 0, currS[prevW] + v)
        currS = nextS

    # 価値の総和の最大値を求める
    maxV = 0
    for prevW in currS:
        maxV = max(maxV, currS[prevW])
    print(maxV)

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
