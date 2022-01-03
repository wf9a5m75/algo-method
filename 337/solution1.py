N, M = list(map(int, input().split()))
W = list(map(int, input().split()))
dp = [[0] * (M + 1) for _ in range(N + 1)]

# weight = 0
dp[0][0] = 1

for i in range(N):
	for j in range(M):
		if dp[i][j] > 0:
			dp[i + 1][j] = 1
			if j + W[i] <= M:
				dp[i + 1][j + W[i]] = 1
# 	print(dp[i])
# print(dp[N])
outputs = ["No", "Yes"]
print(outputs[ dp[N][M] ])
