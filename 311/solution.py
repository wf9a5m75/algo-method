from io import StringIO
import sys

def main():
    N, M = list(map(int, input().split()))
    A = list(map(int, input().split()))

    # 総和0は0通り
    currS = {0: 0}

    for num in A:
        nextS = {}

        # 前の状態に対して処理を行う
        for prevS in currS:
            # 足さない選択肢
            if prevS not in nextS:
                nextS[prevS] = currS[prevS]
            else:
                # 他の組合せと衝突する場合は、組み合わせの数が少ない方を選ぶ
                nextS[prevS] = min(nextS[prevS], currS[prevS])

            # 足す選択肢
            tmp = prevS + num
            if tmp <= M:
                if tmp not in nextS:
                    nextS[tmp] = currS[prevS] + 1
                else:
                    nextS[tmp] = min(nextS[tmp], currS[prevS] + 1)
        currS = nextS
    print(currS.get(M) or -1)

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
