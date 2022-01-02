N = int(input())

# If文を省略するために左右に余白を付ける
prevRow = list(map(int, input().split()))
prevRow.insert(0, 0)
prevRow.append(0)

for i in range(N - 1):

	# 次の行を作る
	nextRow = [0]
	for j in range(1, N + 1):
		nextRow.append(prevRow[j - 1] + prevRow[j] + prevRow[j + 1])
	nextRow.append(0)

	# 作成した結果を次の計算のときに前の行として利用する
	prevRow = nextRow

# modulo は最後にまとめて計算
print(prevRow[N] % 100)
