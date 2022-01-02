N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

# 初日はどの仕事でもOK
today = A[0]
for i in range(1, N):
	# 次の日のパターンを作成する
	today = [
        max(today[1], today[2]) + A[i][0],
        max(today[0], today[2]) + A[i][1],
        max(today[0], today[1]) + A[i][2]
    ]
print(max(today))
