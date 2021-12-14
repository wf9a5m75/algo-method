from io import StringIO
import sys

def main():
    N, M, K = list(map(int, input().split()))
    A = list(map(int, input().split()))

    currS = {0: 0}

    for num in A:
        # 整数を足さない場合は同じなので、前の状態をコピー
        nextS = currS.copy()
        for prevM in currS:
            tmp = prevM + num
            v = currS.get(prevM) + 1

            # 総和がM以下で
            # K個以内の組み合わせなら足す
            if (tmp <= M) and  (v <= K):
                nextS[tmp] = min(nextS.get(tmp) or v, v)
        currS = nextS

    print("Yes" if M in currS else "No")

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
