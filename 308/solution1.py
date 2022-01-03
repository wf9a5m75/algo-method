N, W = list(map(int, input().split()))

dp = [[-1] * (W + 1) for _ in range(N + 1)]
dp[0][0] = 0
for i in range(N):
	w, v = list(map(int, input().split()))

	for j in range(W + 1):
		if (dp[i][j] == -1):
			continue
		dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
		if (j + w <= W):
			dp[i + 1][j + w] = max(dp[i + 1][j + w], dp[i][j] + v)

ans = max(dp[N])
print(ans)
