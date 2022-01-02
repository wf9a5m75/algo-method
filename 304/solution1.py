N = int(input())
dp = [0] * (N + 3)

# 0段目は1通り
dp[0] = 1

for i in range(N):
	# 1段登る
	dp[i + 1] += dp[i]
	# 2段登る
	dp[i + 2] += dp[i]
print(dp[N])
