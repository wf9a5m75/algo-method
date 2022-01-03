N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
dp = [[0] * (M + 1) for _ in range(N + 1)]

# 総和 = 0の状態からスタート
dp[0][0] = 1

for i in range(N):
    for j in range(M + 1):
        if (dp[i][j] == 0):
            continue
        # 足さない
        dp[i + 1][j] = 1

        # 足す
        if (j + A[i] <= M):
            dp[i + 1][j + A[i]] = 1
print(["No", "Yes"][ dp[N][M] ])
