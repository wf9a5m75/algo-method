N = int(input())

# 初日はどの仕事でもOK
today = list(map(int, input().split()))
for i in range(1, N):
	A = list(map(int, input().split()))
	# 次の日のパターンを作成する
	today = [
        max(today[1], today[2]) + A[0],
        max(today[0], today[2]) + A[1],
        max(today[0], today[1]) + A[2]
    ]
print(max(today))
