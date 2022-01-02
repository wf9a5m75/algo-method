N = int(input())
A = list(map(int, input().split()))
INF = 10000000
dp = [INF] * N
dp[0] = 0

for i in range(N):

	# i + 1にジャンプできるなら現在の秒数(dp[i]) + A[i + 1])を保存する
	# ただし、他のルートにより更に短い時間でたどり着ける可能性があるので
	# 最小値を選ぶ
	if (i + 1 < N):
		dp[i + 1] = min(dp[i + 1], dp[i] + A[i + 1])

	# i + 2にジャンプできるなら現在の秒数(dp[i]) + A[i + 2] * 2)を保存する
	# ただし、他のルートにより更に短い時間でたどり着ける可能性があるので
	# 最小値を選ぶ
	if (i + 2 < N):
		dp[i + 2] = min(dp[i + 2], dp[i] + A[i + 2] * 2)
print(dp[N - 1])
