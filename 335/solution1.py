N = int(input())
A = [list(map(int, input().split())) for _  in range(N)]
INF = 100000000
dp = [[INF] * N for _ in range(N)]

dp[0][N - 1] = A[0][N - 1]
for i in range(N):
	for j in range(N - 1, -1, -1):
		if j > 0:
			dp[i][j - 1] = min(dp[i][j - 1], dp[i][j] + A[i][j - 1])
		if i < N - 1:
			dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + A[i + 1][j])
print(dp[N - 1][0])
