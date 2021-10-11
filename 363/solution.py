from io import StringIO
import sys

def main():
    n = int(input())
    schedules = []
    for i in range(n):
        s, t = list(map(int, input().split()))
        schedules.append((s, t))

    # Sorting by the end time
    schedules.sort(key = lambda x: x[1])

    curr = None
    ans = 0
    for schedule in schedules:
        if curr is not None:
            if curr[1] <= schedule[0]:
                # The curr has been already done
                curr = None
            else:
                # The curr has been still going on
                continue
        # There is no schedule at this time.
        curr = schedule
        ans += 1
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
