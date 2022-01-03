N, M = list(map(int, input().split()))
W = list(map(int, input().split()))
INF = 100000000
dp = [[INF] * (M + 1) for _ in range(N + 1)]

# ボールが何も入っていない状態
dp[0][0] = 0
for i in range(N):
	for j in range(M + 1):
		if dp[i][j] == INF:
			continue

		# ボールを追加しなかった
		dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])

		# ボールを追加した
		if (j + W[i] <= M):
			dp[i + 1][j + W[i]] = min(dp[i + 1][j + W[i]], dp[i][j] + 1)
if dp[N][M] == INF:
	print(-1)
else:
	print(dp[N][M])
