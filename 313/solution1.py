N, M = list(map(int, input().split()))
INF = 10000000
dp = [[INF] * (M + 1) for _ in range(N + 1)]

# The situation that we have no elements and the summation 0 is True
dp[0][0] = 0
for i in range(N):
	A, B = list(map(int, input().split()))

	for j in range(M + 1):
		if dp[i][j] == INF:
			continue
		dp[i + 1][j] = 0

		# Keeping the number of usage of A in the cell
		if (dp[i][j] < B) and (j + A <= M):
			dp[i][j + A] = dp[i][j] + 1
			dp[i + 1][j + A] = 0

	if dp[i + 1][M] < INF:
		dp[N][M] = 1
		break
	#print(dp[i])
#print(dp[N])
if dp[i + 1][M] < INF:
    print("Yes")
else:
    print("No")
# print(["No", "Yes"][ dp[N][M] ])
