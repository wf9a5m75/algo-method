N, M = list(map(int, input().split()))
D = list(map(int, input().split()))
dp = [False] * (N + 1)

# スタート地点は既に到達しているのでTrue
dp[0] = True

for i in range(N + 1):

	# dp[i] には辿り着いていない
	if dp[i] == False:
		continue

	# 可能な出目を全て試す
	for d in D:
		if i + d <= N:
			dp[i + d] = True

# 最後に辿り着いているか？
print(["No", "Yes"][int(dp[N])])
