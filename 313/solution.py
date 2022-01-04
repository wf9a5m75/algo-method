from io import StringIO
import sys

def main():
    N, M = list(map(int, input().split()))
    dp = [[0] * (M + 1) for _ in range(N + 1)]

    # The situation that we have no elements and the summation 0 is True
    dp[0][0] = 1
    for i in range(N):
        A, B = list(map(int, input().split()))

        for j in range(M + 1):
            if dp[i][j] == 0:
                continue

            # We don't add the A[i]
            # dp[i + 1][j] = 1

            # If we can still add the A[i], add it
            for b in range(B + 1):
                if (j + A * b <= M):
                    dp[i + 1][j + A * b] = 1
                else:
                    break
            if dp[i + 1][M] == 1:
                dp[N][M] = 1
                break
    #     print(dp[i])
    # print(dp[N])
    print(["No", "Yes"][ dp[N][M] ])

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
