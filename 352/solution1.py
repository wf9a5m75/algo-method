N, A, B = list(map(int, input().split()))
B1 = B + 1
X = list(map(int, input().split()))
INF = 0
dp = [[INF] * A for _ in range(N + 1)]

# 何もカードを選んでいない状態は成立する
dp[0][0] = 1

for i in range(N):
	for j in range(A):
		if (dp[i][j] == INF):
			continue

		# カードを選ばない状態
		dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])

		# カードを選んだ状態
		dp[i + 1][(j + X[i]) % A] = 1
print(["No","Yes"][ dp[N][B]] )
