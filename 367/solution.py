from io import StringIO
import sys

def main():
    N, M = list(map(int, input().split()))

    left = 0
    right = 100
    while(right - left > 1e-6):
        x = (left + right) / 2
        s = N + 1
        for i in range(5):
            s = s * x + 1

        if s > M:
            right = x
        else:
            left = x
    print(left)



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
        try:
            ansLine = ansLine.strip()
            ans = float(ansLine)
            result = float(results[i])
            if abs(ans - result) <= 0.01:
                results[i] = "   |" + results[i]
            else:
                results[i] = "-->|" + results[i]
                passTheTest = False
        except:
            results[i] = "-->|" + results[i]
            passTheTest = False

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
