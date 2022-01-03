N,M = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
dp = [[-1] * M for _ in range(N)]

dp[0][0] = 0
for i in range(N - 1):
	for j in range(M):
		if dp[i][j] > -1:
			dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
			if (j + A[i] < M):
				dp[i + 1][j + A[i]] = max(dp[i + 1][j + A[i]], dp[i][j] + B[i])
print(dp[N - 1][M - 1])
