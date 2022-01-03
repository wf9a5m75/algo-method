N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
INF = 100000
dp = [[INF] * (M + 1) for _ in range(N + 1)]

# 何も入っていない状態 ( = 0個の整数の組み合わせ )
dp[0][0] = 0

for i in range(N):
	for j in range(M + 1):
		if dp[i][j] == INF:
			continue
		# 何も足さない
		dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])

		# A[i]を1つ足す
		if (j + A[i] <= M):
			dp[i + 1][j + A[i]] = min(dp[i + 1][j + A[i]], dp[i][j] + 1)
if dp[N][M] == INF:
	print(-1)
else:
	print(dp[N][M])
