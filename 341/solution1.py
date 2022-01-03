N, M = list(map(int, input().split()))
W = list(map(int, input().split()))
V = list(map(int, input().split()))
dp = [[-1] * (M + 1) for _ in range(N + 1)]

dp[0][0] = 0
for i in range(N):
	for j in range(M + 1):
		if dp[i][j] == -1:
			continue
		# ボールを入れなかった場合
		dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])

		# ボールを入れた場合
		if j + W[i] <= M:
			dp[i + 1][j + W[i]] = max(dp[i + 1][j + W[i]], dp[i][j] + V[i])

ans = max(dp[N])
if (ans == -1):
	print(0)
else:
	print(ans)
