N = int(input())
N1 = N + 1
dp = [[0] * N1 for _ in range(N1)]

dp[0][0] = 1
for i in range(N):
	for j in range(N):
		dp[i + 1][j] += dp[i][j]
		dp[i][j + 1] += dp[i][j]
print(dp[N - 1][N - 1])
