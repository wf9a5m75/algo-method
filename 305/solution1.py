N = int(input())
dp = [0] * (N + 3)

# 最初は1通り
dp[0] = 1

for i in range(N):
	# 1x1のタイル
	dp[i + 1] += dp[i]
	# 1x2のタイル
	dp[i + 2] += dp[i]
	# 1x3のタイル
	dp[i + 3] += dp[i]

print(dp[N])
