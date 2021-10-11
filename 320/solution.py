from io import StringIO
import sys
import math

def isPrime(N):
    if N <= 3:
        if N > 1:
            return True
        return False
    if (N & 1 == 0) or (N % 3 == 0):
        return False

    upper = math.sqrt(N)

    i = 5
    while(i <= upper):
        if (N % i == 0) or (N % (i + 2) == 0):
            return False
        i += 6
    return True

def main():
    i = int(input())
    if i == 2:
        print(2)
    else:
        if i & 1 == 0:
            i -= 1
        while(i > 0):
            if (isPrime(i)):
                print(i)
                break
            i -= 2

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
    test2()
