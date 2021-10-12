from io import StringIO
import sys

def summation(N):
    return (N*(N+1)) >> 1

def solve(target):
    # 0から X日(Xはtargetを達成しうる十分に大きな日数)の中で
    # 効率よく( O(logX) )、貯金 >= target金額 になる日にちを探す
    left = 0
    right = target
    s = 0
    while(right - left > 0):
        mid = (left + right) >> 1

        # mid 日目の貯金額を計算する
        s = summation(mid)

        if (s == target):
            return mid

        # 貯金額がtarget金額より少なければ、leftを増やす
        if s < target:
            left = mid + 1

        # 貯金額がtarget金額より多ければ、rightを減らす
        else:
            right = mid
    return left


def main():
    N = int(input())
    A = list(map(int, input().split()))
    for target in A:
        print(solve(target))



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
