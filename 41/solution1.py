N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

# 初日はどの仕事でもOK
today = A[0]

for i in range(1, N):
	tomorrow = [0, 0, 0]
	for j in range(3):
		k = (j - 1) % 3
		tomorrow[k] = max(tomorrow[k], today[j] + A[i][k])
		k = (j + 1) % 3
		tomorrow[k] = max(tomorrow[k], today[j] + A[i][k])
	today = tomorrow
print(max(today))
