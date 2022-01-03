N,M = list(map(int, input().split()))
A = list(map(int, input().split()))

dp = [[0] * (M + 1) for _ in range(N + 1)]

# 整数を何も選んでいない & 総和0が1通り
dp[0][0] = 1

for i in range(N):
	for j in range(M + 1):
		if dp[i][j] == 0:
			continue
		dp[i + 1][j] += dp[i][j]

		if (j + A[i] <= M):
			dp[i + 1][j + A[i]] += dp[i][j]
print(dp[N][M] % 1000)
