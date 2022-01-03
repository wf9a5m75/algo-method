N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
dp = [[0] * M for _ in range(N)]

dp[0][0] = 1
for i in range(N - 1):
    for j in range(M):
        if dp[i][j] > 0:
            dp[i + 1][j] = 1
            if j + A[i] < M:
                dp[i + 1][j + A[i]] = 1

print(sum(dp[N - 1]))
