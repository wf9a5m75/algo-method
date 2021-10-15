from io import StringIO
import sys

def binarySearch(A, target, left, right):
    while(left != right):
        mid = (left + right) >> 1
        if A[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

def main():
    x,y,z = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    A.sort()

    ans = 0
    for c in C:
        for b in B:
            expectA = c - b
            if (expectA < A[0]) or (expectA > A[-1]):
                continue
            pos = binarySearch(A, expectA, 0, x)
            # print("{} - {} = {}, pos = {}".format(c, b, expectA, pos))
            if (pos < x) and (A[pos] == expectA):
                pos1 = binarySearch(A, expectA + 1, pos, x)
                pos1 = min(pos1, x - 1)
                if A[pos1] != expectA:
                    pos1 -= 1

                ans += pos1 - pos + 1
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
