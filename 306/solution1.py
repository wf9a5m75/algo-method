N,M = list(map(int, input().split()))
A = list(map(int, input().split()))

INF = 1000000
dp = [INF] * N
dp[0] = 0
for i in range(N):

	# 移動できる範囲内を全て計算する
	for j in range(i + 1, min(N, i + M + 1)):
		dp[j] = min(dp[j], dp[i] + A[j] * (j - i))
print(dp[N - 1])
