N, M, K = list(map(int, input().split()))
A = list(map(int, input().split()))

INF = 100000
dp = [[INF] * (M + 1) for _ in range(N + 1)]

# Summation 0 is zero number of combination
dp[0][0] = 0

for i in range(N):

	for j in range(M + 1):
		if dp[i][j] == INF:
			continue

		dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])

		# Adds one value if possible
		if (j + A[i] <= M) and (dp[i][j] + 1 <= K):
			dp[i + 1][j + A[i]] = min(dp[i + 1][j + A[i]], dp[i][j] + 1)
if dp[N][M] != INF:
	print("Yes")
else:
	print("No")
