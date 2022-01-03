N = int(input())
W = list(map(int, input().split()))
maxW = sum(W)

dp = [[False] * (maxW + 1) for i in range(N + 1)]

# 最初は両方の箱に何も入っていない状態
dp[0][0] = True

for i in range(N):
	for j in range(maxW):
		if dp[i][j] == False:
			continue

		# 箱1にボールを入れた
		dp[i + 1][j + W[i]] = True

		# 箱2にボールを入れた(=箱1にボールを入れなかった)
		dp[i + 1][abs(j - W[i])] = True

j = 0
while(dp[N][j] == False):
	j+=1
print(j)
