from io import StringIO
import sys

def binarySearch(A, target, left, right):
    while(left != right):
        mid = (left + right) >> 1
        if A[mid] > target:
            right = mid
        else:
            left = mid + 1
    return left

def main():

    sizeA, sizeB = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    B.sort()

    # 1 4 6
    # 3 4 7
    ans = 0
    for i in range(sizeA):
        pos = binarySearch(B, A[i] - 1, 0, sizeB)
        # print(A[i], pos, ans)
        if pos == 0:
            continue
        if pos == sizeB:
            ans += pos
            continue
        while(pos > 0) and (B[pos] >= A[i]):
            pos -= 1
        ans += pos + 1
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
    test2()
