from io import StringIO
import sys

def main():
    S = input()
    T = input()
    lenS, lenT = len(S), len(T)

    dp = [[0] * (lenS + 1) for _ in range(lenT + 1)]
    ans = 0
    for i in range(lenT):
        for j in range(lenS):
            if T[i] == S[j]:
                # dp[i + 1][j + 1] = max(dp[i][j + 1] + 1, dp[i + 1][j] + 1)と同じ
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
        ans = max(ans, dp[i + 1][lenS])
    #     print(dp[i])
    # print(dp[lenT])
    print(ans)

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
