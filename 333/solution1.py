N = int(input())
dp = [[0] * N for _ in range(N)]

sMap = [input() for _ in range(N)]
dp[0][0] = 1

for i in range(N):
	for j in range(N):
		if (j + 1 < N) and (sMap[i][j + 1] == "."):
			dp[i][j + 1] += dp[i][j]
		if (i + 1 < N) and (sMap[i + 1][j] == "."):
			dp[i + 1][j] += dp[i][j]
print(dp[N - 1][N - 1])
