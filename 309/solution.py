from io import StringIO
import sys

def main():
    N, M = list(map(int, input().split()))
    A = list(map(int, input().split()))

    currS = set()
    currS.add(0)

    for num in A:
        nextS = set()
        for prevS in currS:
            # numを足さない
            nextS.add(prevS)

            # Mを超えないならnumを足す
            if prevS + num <= M:
                nextS.add(prevS + num)
        currS = nextS

    print("Yes" if M in currS else "No")

def another_solution():
    N, M = list(map(int, input().split()))
    A = list(map(int, input().split()))

    # 0ビット目を１にする
    # (= 総和0は成立する)
    dp = 1

    # 最大値
    upper = 1 << M

    for num in A:

        tmpDP = dp
        i = 0
        while(tmpDP > 0):
            if (tmpDP & 1 == 1):
                # Mを超えないならnumを足す
                if i + num <= upper:
                    # i + numビット目を1にする
                    dp |= 1 << (i + num)
            i += 1
            tmpDP >>= 1

    print("Yes" if (dp & upper > 0) else "No")

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
